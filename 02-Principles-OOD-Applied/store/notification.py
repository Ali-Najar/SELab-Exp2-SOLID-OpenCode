from store.contracts import Notifier


class EmailNotifier(Notifier):
    def send(self, customer, message: str) -> None:
        print(f"[email] to {customer.email}: {message}")


class SmsNotifier(Notifier):
    def send(self, customer, message: str) -> None:
        print(f"[sms] to {customer.phone}: {message}")


class PushNotifier(Notifier):
    def send(self, customer, message: str) -> None:
        print(f"[push] to {customer.name}: {message}")