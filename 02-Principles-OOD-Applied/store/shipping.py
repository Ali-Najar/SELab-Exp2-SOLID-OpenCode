from store.contracts import ShippingService


class StandardShippingService(ShippingService):
    def calculate(self, order, subtotal: float) -> float:
        return 5.0 if subtotal < 100 else 0.0