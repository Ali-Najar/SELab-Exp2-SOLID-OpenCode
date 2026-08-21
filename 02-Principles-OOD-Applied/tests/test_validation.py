import unittest

from store.models import BundleOrder, Customer, Order, OrderItem
from store.validation import DefaultOrderValidator


def make_order(*items, payment_method="credit_card"):
    return Order(
        id=1,
        customer=Customer(id=1, name="A", email="a@x.com"),
        items=list(items),
        payment_method=payment_method,
    )


class DefaultOrderValidatorTests(unittest.TestCase):
    def test_empty_items_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            DefaultOrderValidator().validate(make_order())

        self.assertEqual(str(ctx.exception), "Order has no items")

    def test_missing_payment_method_rejected(self):
        order = make_order(OrderItem(1, "X", 1.0, 1), payment_method="")

        with self.assertRaises(ValueError) as ctx:
            DefaultOrderValidator().validate(order)

        self.assertEqual(str(ctx.exception), "Order has no payment method")

    def test_valid_order_passes(self):
        DefaultOrderValidator().validate(make_order(OrderItem(1, "X", 1.0, 1)))

    def test_empty_bundle_rejected_like_empty_order(self):
        bundle = BundleOrder(id=2, customer=Customer(id=1, name="A", email="a@x.com"), orders=[])

        with self.assertRaises(ValueError) as ctx:
            DefaultOrderValidator().validate(bundle)

        self.assertEqual(str(ctx.exception), "Order has no items")

    def test_populated_bundle_validates_as_plain_order(self):
        child = make_order(OrderItem(1, "X", 1.0, 1))
        bundle = BundleOrder(id=3, customer=child.customer, orders=[child])
        bundle.payment_method = "paypal"

        DefaultOrderValidator().validate(bundle)


if __name__ == "__main__":
    unittest.main()
