class VipDiscountRule:
    def applies(self, order):
        return order.customer.is_vip

    def calculate(self, order):
        return order.subtotal * 0.20


class BulkDiscountRule:
    def applies(self, order):
        return order.item_count >= 10

    def calculate(self, order):
        return order.subtotal * 0.10


class WelcomeCouponDiscountRule:
    def applies(self, order):
        return "WELCOME10" in order.coupons

    def calculate(self, order):
        return order.subtotal * 0.10


class RuleBasedDiscountCalculator:
    def __init__(self, rules=None):
        if rules is None:
            rules = [
                VipDiscountRule(),
                BulkDiscountRule(),
                WelcomeCouponDiscountRule(),
            ]
        self.rules = list(rules)

    def calculate(self, order):
        for rule in self.rules:
            if rule.applies(order):
                return round(rule.calculate(order), 2)

        return 0.0