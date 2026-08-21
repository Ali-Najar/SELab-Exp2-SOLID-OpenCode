import io
import unittest
from contextlib import redirect_stdout

from store.contracts import PaymentMethod
from store.models import Customer, Order
from store.payment import (
    BitcoinPayment,
    CashPayment,
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
            build_processor().process(make_order("crypto"), 10.0)

        self.assertEqual(str(ctx.exception), "Unknown payment method: 'crypto'")

    def test_new_methods_plug_in_without_modifying_processor(self):
        class BarterPayment(PaymentMethod):
            @property
            def key(self) -> str:
                return "barter"

            def pay(self, order, amount: float) -> str:
                return f"paid_by_barter:{amount:.2f}"

        processor = PaymentProcessor([
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
            BarterPayment(),
        ])

        receipt = processor.process(make_order("barter"), 7.5)

        self.assertEqual(receipt, "paid_by_barter:7.50")


class CashPaymentTests(unittest.TestCase):
    def build_cash_processor(self):
        return PaymentProcessor([
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
            CashPayment(),
        ])

    def test_cash_payment_prints_and_returns_receipt(self):
        order = make_order("cash")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            receipt = self.build_cash_processor().process(order, 12.5)

        self.assertEqual(receipt, "paid_by_cash:12.50")
        self.assertIn("[payment] Cash payment 12.50", buffer.getvalue())

    def test_cash_plugs_into_unmodified_processor(self):
        order = make_order("cash")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            receipt = self.build_cash_processor().process(order, 3.0)

        self.assertEqual(receipt, "paid_by_cash:3.00")


if __name__ == "__main__":
    unittest.main()
