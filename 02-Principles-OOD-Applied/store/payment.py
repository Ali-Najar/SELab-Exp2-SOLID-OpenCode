from typing import Iterable

from store.contracts import PaymentMethod, PaymentService


class CreditCardPayment(PaymentMethod):
    @property
    def key(self) -> str:
        return "credit_card"

    def pay(self, order, amount: float) -> str:
        card = order.customer.credit_card
        print(f"[payment] Charging card {card} {amount:.2f}")
        return f"paid_by_credit_card:{amount:.2f}"


class PayPalPayment(PaymentMethod):
    @property
    def key(self) -> str:
        return "paypal"

    def pay(self, order, amount: float) -> str:
        email = order.customer.email
        print(f"[payment] Charging PayPal {email} {amount:.2f}")
        return f"paid_by_paypal:{amount:.2f}"


class BitcoinPayment(PaymentMethod):
    @property
    def key(self) -> str:
        return "bitcoin"

    def pay(self, order, amount: float) -> str:
        address = order.customer.bitcoin_address
        print(f"[payment] Charging BTC {address} {amount:.2f}")
        return f"paid_by_bitcoin:{amount:.2f}"


class PaymentProcessor(PaymentService):
    def __init__(self, methods: Iterable[PaymentMethod]):
        self._methods = {
            method.key: method
            for method in methods
        }

    def process(self, order, amount: float) -> str:
        method = self._methods.get(order.payment_method)

        if method is None:
            raise ValueError(
                f"Unknown payment method: {order.payment_method!r}"
            )

        return method.pay(order, amount)