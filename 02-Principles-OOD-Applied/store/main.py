from store.models import BundleOrder, Customer, Order, OrderItem
from store.notification import EmailNotifier, SmsNotifier
from store.order_service import OrderService
from store.payment import (
    BitcoinPayment,
    CreditCardPayment,
    PayPalPayment,
    PaymentProcessor,
)
from store.pricing import (
    BulkDiscountRule,
    RuleBasedDiscountCalculator,
    VipDiscountRule,
    WelcomeCouponDiscountRule,
)
from store.receipt import ConsoleReceiptPrinter
from store.shipping import StandardShippingService
from store.storage import MySqlDatabase
from store.validation import DefaultOrderValidator


def build_demo_orders():
    vip = Customer(
        id=1, name="Alice", email="alice@example.com",
        phone="555-0100", is_vip=True, credit_card="4111 1111 1111 1111",
    )
    regular = Customer(
        id=2, name="Bob", email="bob@example.com", phone="555-0199",
    )

    laptop = Order(
        id=101, customer=vip, payment_method="credit_card",
        items=[OrderItem(1, "Laptop", 999.99, 1),
               OrderItem(2, "Mouse", 25.00, 1)],
    )

    books = Order(
        id=102, customer=regular, payment_method="paypal",
        items=[OrderItem(3, "Clean Code", 45.00, 2),
               OrderItem(4, "Pragmatic Programmer", 40.00, 2)],
    )

    bundle = BundleOrder(id=103, customer=vip, orders=[laptop, books])
    bundle.payment_method = "credit_card"
    return laptop, books, bundle


def build_order_service() -> OrderService:
    return OrderService(
        validator=DefaultOrderValidator(),
        pricing=RuleBasedDiscountCalculator([
            VipDiscountRule(),
            BulkDiscountRule(),
            WelcomeCouponDiscountRule(),
        ]),
        shipping=StandardShippingService(),
        payment=PaymentProcessor([
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
        ]),
        repository=MySqlDatabase(),
        notifiers=[EmailNotifier(), SmsNotifier()],
        receipt_printer=ConsoleReceiptPrinter(),
    )


def main() -> None:
    service = build_order_service()
    laptop, books, bundle = build_demo_orders()

    print(">>> Checkout a simple order")
    service.process_order(laptop)

    print("\n>>> Checkout a bundle of two orders")
    service.process_order(bundle)


if __name__ == "__main__":
    main()
