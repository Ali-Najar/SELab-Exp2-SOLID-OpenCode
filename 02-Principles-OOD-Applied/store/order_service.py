class OrderService:
    def __init__(
        self,
        validator,
        pricing,
        shipping,
        payment,
        repository,
        notifiers,
        receipt_printer,
    ):
        self.validator = validator
        self.pricing = pricing
        self.shipping = shipping
        self.payment = payment
        self.repository = repository
        self.notifiers = list(notifiers)
        self.receipt_printer = receipt_printer

    def process_order(self, order, notify=True):
        self.validator.validate(order)

        subtotal = order.subtotal

        discount = self.pricing.calculate(order)

        shipping = self.shipping.calculate(
            order,
            subtotal,
        )

        total = round(
            subtotal - discount + shipping,
            2,
        )

        receipt = self.payment.process(
            order,
            total,
        )

        order.status = "paid"

        self.repository.save_order(order)

        if notify:
            message = (
                f"Order {order.id} total "
                f"${total:.2f} ({receipt})"
            )

            for notifier in self.notifiers:
                notifier.send(
                    order.customer,
                    message,
                )

        self.receipt_printer.print_receipt(
            order,
            subtotal,
            discount,
            shipping,
            total,
            receipt,
        )

        return order