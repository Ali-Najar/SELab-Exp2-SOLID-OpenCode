import unittest

from store.models import BundleOrder, Customer, Order, OrderItem


def make_customer(**overrides):
    data = dict(id=1, name="Alice", email="alice@example.com", phone="555-0100")
    data.update(overrides)
    return Customer(**data)


def make_order(order_id, *items):
    return Order(id=order_id, customer=make_customer(), items=list(items))


class BundleOrderTests(unittest.TestCase):
    def test_bundle_flattens_child_items(self):
        child_a = make_order(1, OrderItem(10, "A", 10.0, 2))
        child_b = make_order(2, OrderItem(11, "B", 5.0, 1))

        bundle = BundleOrder(id=3, customer=make_customer(), orders=[child_a, child_b])

        self.assertEqual(len(bundle.items), 2)
        self.assertEqual(bundle.subtotal, 25.0)
        self.assertEqual(bundle.item_count, 3)

    def test_nested_bundles_flatten_recursively(self):
        leaf = make_order(1, OrderItem(10, "A", 10.0, 1))
        inner = BundleOrder(id=2, customer=make_customer(), orders=[leaf])
        other = make_order(3, OrderItem(11, "B", 1.0, 2))

        outer = BundleOrder(id=4, customer=make_customer(), orders=[inner, other])

        self.assertEqual(len(outer.items), 2)
        self.assertEqual(outer.subtotal, 12.0)
        self.assertEqual(outer.item_count, 3)

    def test_empty_bundle_behaves_like_empty_order(self):
        bundle = BundleOrder(id=5, customer=make_customer(), orders=[])

        self.assertEqual(bundle.items, [])
        self.assertEqual(bundle.subtotal, 0)
        self.assertEqual(bundle.item_count, 0)

    def test_bundle_substitutes_for_order_in_pricing_inputs(self):
        child_a = make_order(1, OrderItem(10, "A", 100.0, 6))
        child_b = make_order(2, OrderItem(11, "B", 100.0, 5))

        bundle = BundleOrder(id=3, customer=make_customer(is_vip=False), orders=[child_a, child_b])

        self.assertGreaterEqual(bundle.item_count, 10)
        self.assertEqual(bundle.subtotal, 1100.0)


if __name__ == "__main__":
    unittest.main()
