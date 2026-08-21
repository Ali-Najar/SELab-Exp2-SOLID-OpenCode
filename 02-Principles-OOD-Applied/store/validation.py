from store.contracts import OrderValidator


class DefaultOrderValidator(OrderValidator):
    def validate(self, order) -> None:
        if not order.items:
            raise ValueError("Order has no items")

        if not order.payment_method:
            raise ValueError("Order has no payment method")