import io
import unittest
from contextlib import redirect_stdout

from store.contracts import PaymentMethod
from store.models import Customer, Order
from store.payment import (
    BitcoinPayment,
    CreditCardPayment,
    PayPalPayment,
    PaymentProcessor,
)


def make_order(method):
    customer = Customer(
        id=1,
        name="Alice",
        email="alice@example.com",
        phone="555-0100",
        credit_card="4111 1111 1111 1111",
        bitcoin_address="bc1qexample",
    )
    return Order(id=1, customer=customer, payment_method=method)


def build_processor():
    return PaymentProcessor([
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
    ])


class PaymentStrategyTests(unittest.TestCase):
    def test_credit_card_charges_card(self):
        order = make_order("credit_card")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            receipt = build_processor().process(order, 10.0)

        self.assertEqual(receipt, "paid_by_credit_card:10.00")
        self.assertIn("[payment] Charging card 4111 1111 1111 1111 10.00", buffer.getvalue())

    def test_paypal_charges_email(self):
        order = make_order("paypal")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            receipt = build_processor().process(order, 10.0)

        self.assertEqual(receipt, "paid_by_paypal:10.00")
        self.assertIn("[payment] Charging PayPal alice@example.com 10.00", buffer.getvalue())

    def test_bitcoin_charges_address(self):
        order = make_order("bitcoin")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            receipt = build_processor().process(order, 10.0)

        self.assertEqual(receipt, "paid_by_bitcoin:10.00")
        self.assertIn("[payment] Charging BTC bc1qexample 10.00", buffer.getvalue())

    def test_unknown_method_raises_value_error(self):
        with self.assertRaises(ValueError) as ctx:
            build_processor().process(make_order("cash"), 10.0)

        self.assertEqual(str(ctx.exception), "Unknown payment method: 'cash'")

    def test_new_methods_plug_in_without_modifying_processor(self):
        class CashPayment(PaymentMethod):
            @property
            def key(self) -> str:
                return "cash"

            def pay(self, order, amount: float) -> str:
                return f"paid_by_cash:{amount:.2f}"

        processor = PaymentProcessor([
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
            CashPayment(),
        ])

        receipt = processor.process(make_order("cash"), 7.5)

        self.assertEqual(receipt, "paid_by_cash:7.50")


if __name__ == "__main__":
    unittest.main()
