import unittest

from store.models import Customer, Order, OrderItem
from store.pricing import (
    BulkDiscountRule,
    RuleBasedDiscountCalculator,
    VipDiscountRule,
    WelcomeCouponDiscountRule,
)


def make_order(*items, is_vip=False, coupons=None):
    customer = Customer(id=1, name="Alice", email="a@x.com", is_vip=is_vip)
    return Order(
        id=1,
        customer=customer,
        items=list(items),
        coupons=list(coupons or []),
    )


class DiscountPrecedenceTests(unittest.TestCase):
    def test_vip_discount_wins_over_bulk_and_coupon(self):
        order = make_order(
            OrderItem(1, "X", 10.0, 12),
            is_vip=True,
            coupons=["WELCOME10"],
        )

        discount = RuleBasedDiscountCalculator().calculate(order)

        self.assertEqual(discount, 24.0)

    def test_bulk_discount_when_not_vip(self):
        order = make_order(OrderItem(1, "X", 10.0, 10))

        discount = RuleBasedDiscountCalculator().calculate(order)

        self.assertEqual(discount, 10.0)

    def test_coupon_discount_when_not_vip_and_below_bulk(self):
        order = make_order(
            OrderItem(1, "X", 40.0, 1),
            coupons=["WELCOME10"],
        )

        discount = RuleBasedDiscountCalculator().calculate(order)

        self.assertEqual(discount, 4.0)

    def test_no_rule_applies_returns_zero(self):
        order = make_order(OrderItem(1, "X", 40.0, 1))

        discount = RuleBasedDiscountCalculator().calculate(order)

        self.assertEqual(discount, 0.0)

    def test_only_one_discount_is_ever_applied(self):
        order = make_order(
            OrderItem(1, "X", 10.0, 20),
            is_vip=True,
            coupons=["WELCOME10"],
        )

        discount = RuleBasedDiscountCalculator().calculate(order)

        self.assertEqual(discount, 40.0)

    def test_first_match_wins_is_caller_controlled(self):
        order = make_order(
            OrderItem(1, "X", 10.0, 12),
            is_vip=True,
            coupons=["WELCOME10"],
        )
        coupon_first = RuleBasedDiscountCalculator([
            WelcomeCouponDiscountRule(),
            VipDiscountRule(),
        ])

        self.assertEqual(coupon_first.calculate(order), 12.0)

    def test_default_rules_match_baseline_precedence(self):
        order = make_order(
            OrderItem(1, "X", 10.0, 12),
            is_vip=True,
            coupons=["WELCOME10"],
        )

        self.assertEqual(RuleBasedDiscountCalculator().calculate(order), 24.0)

    def test_discount_is_rounded_to_cents(self):
        order = make_order(
            OrderItem(1, "Laptop", 999.99, 1),
            OrderItem(2, "Mouse", 25.0, 1),
            is_vip=True,
        )

        self.assertEqual(RuleBasedDiscountCalculator().calculate(order), 205.0)


class RuleUnitTests(unittest.TestCase):
    def test_bulk_rule_threshold_is_inclusive_at_ten(self):
        at_threshold = make_order(OrderItem(1, "X", 10.0, 10))
        below_threshold = make_order(OrderItem(1, "X", 10.0, 9))

        rule = BulkDiscountRule()

        self.assertTrue(rule.applies(at_threshold))
        self.assertFalse(rule.applies(below_threshold))

    def test_coupon_rule_requires_exact_code(self):
        matching = make_order(OrderItem(1, "X", 10.0, 1), coupons=["WELCOME10"])
        non_matching = make_order(OrderItem(1, "X", 10.0, 1), coupons=["OTHER"])

        rule = WelcomeCouponDiscountRule()

        self.assertTrue(rule.applies(matching))
        self.assertFalse(rule.applies(non_matching))


if __name__ == "__main__":
    unittest.main()
