import io
import unittest
from contextlib import redirect_stdout

from store.models import Customer, Order, OrderItem
from store.order_service import OrderService
from store.payment import (
    BitcoinPayment,
    CreditCardPayment,
    PayPalPayment,
    PaymentProcessor,
)
from store.pricing import RuleBasedDiscountCalculator
from store.receipt import ConsoleReceiptPrinter
from store.shipping import StandardShippingService
from store.validation import DefaultOrderValidator


class FakeRepository:
    def __init__(self):
        self.saved = []

    def save_order(self, order):
        self.saved.append(order)

    def load_order(self, order_id):
        return next((o for o in self.saved if o.id == order_id), None)


class RecordingNotifier:
    def __init__(self, channel):
        self.channel = channel
        self.calls = []

    def send(self, customer, message):
        self.calls.append((self.channel, customer.id, message))


def make_laptop_order():
    customer = Customer(
        id=1,
        name="Alice",
        email="alice@example.com",
        phone="555-0100",
        is_vip=True,
        credit_card="4111 1111 1111 1111",
    )
    return Order(
        id=101,
        customer=customer,
        payment_method="credit_card",
        items=[
            OrderItem(1, "Laptop", 999.99, 1),
            OrderItem(2, "Mouse", 25.00, 1),
        ],
    )


def build_service(repository=None, notifiers=None):
    return OrderService(
        validator=DefaultOrderValidator(),
        pricing=RuleBasedDiscountCalculator(),
        shipping=StandardShippingService(),
        payment=PaymentProcessor([
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
        ]),
        repository=repository or FakeRepository(),
        notifiers=notifiers or [],
        receipt_printer=ConsoleReceiptPrinter(),
    )


class OrderServiceFlowTests(unittest.TestCase):
    def test_happy_path_prices_charges_persists_notifies(self):
        order = make_laptop_order()
        repository = FakeRepository()
        email = RecordingNotifier("email")
        sms = RecordingNotifier("sms")
        service = build_service(repository, [email, sms])

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = service.process_order(order)

        self.assertIs(result, order)
        self.assertEqual(order.status, "paid")
        self.assertEqual(repository.saved, [order])
        expected_message = "Order 101 total $819.99 (paid_by_credit_card:819.99)"
        self.assertEqual(email.calls, [("email", 1, expected_message)])
        self.assertEqual(sms.calls, [("sms", 1, expected_message)])
        self.assertIn("--- Receipt for order 101 ---", buffer.getvalue())
        self.assertIn("TOTAL       $819.99", buffer.getvalue())

    def test_notify_false_skips_notifiers_but_still_prints_receipt(self):
        order = make_laptop_order()
        email = RecordingNotifier("email")
        service = build_service(notifiers=[email])

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            service.process_order(order, notify=False)

        self.assertEqual(email.calls, [])
        self.assertIn("--- Receipt for order 101 ---", buffer.getvalue())

    def test_unknown_payment_method_aborts_before_persistence(self):
        order = make_laptop_order()
        order.payment_method = "cash"
        repository = FakeRepository()

        with self.assertRaises(ValueError):
            build_service(repository).process_order(order)

        self.assertEqual(order.status, "pending")
        self.assertEqual(repository.saved, [])

    def test_missing_payment_method_rejected_before_any_charge(self):
        order = make_laptop_order()
        order.payment_method = ""
        repository = FakeRepository()

        with self.assertRaises(ValueError) as ctx:
            build_service(repository).process_order(order)

        self.assertEqual(str(ctx.exception), "Order has no payment method")
        self.assertEqual(repository.saved, [])

    def test_shipping_free_at_hundred_subtotal_boundary(self):
        order = Order(
            id=202,
            customer=Customer(id=2, name="Bob", email="b@example.com"),
            payment_method="paypal",
            items=[OrderItem(9, "Gift", 50.0, 2)],
        )

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            build_service().process_order(order)

        self.assertIn("Subtotal    $100.00", buffer.getvalue())
        self.assertIn("Shipping    $0.00", buffer.getvalue())
        self.assertIn("TOTAL       $100.00", buffer.getvalue())

    def test_shipping_charged_below_hundred_subtotal(self):
        order = Order(
            id=203,
            customer=Customer(id=2, name="Bob", email="b@example.com"),
            payment_method="paypal",
            items=[OrderItem(9, "Gift", 49.99, 2)],
        )

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            build_service().process_order(order)

        self.assertIn("Shipping    $5.00", buffer.getvalue())
        self.assertIn("TOTAL       $104.98", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
