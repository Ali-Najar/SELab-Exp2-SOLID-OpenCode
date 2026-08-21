import io
import unittest
from contextlib import redirect_stdout

from store.models import Customer
from store.notification import EmailNotifier, PushNotifier, SmsNotifier


def make_customer():
    return Customer(id=1, name="Alice", email="alice@example.com", phone="555-0100")


class NotifierTests(unittest.TestCase):
    def capture(self, notifier, message="hi"):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            notifier.send(make_customer(), message)
        return buffer.getvalue()

    def test_email_notifier_prints_email_line(self):
        self.assertEqual(self.capture(EmailNotifier()), "[email] to alice@example.com: hi\n")

    def test_sms_notifier_prints_sms_line(self):
        self.assertEqual(self.capture(SmsNotifier()), "[sms] to 555-0100: hi\n")

    def test_push_notifier_prints_push_line(self):
        self.assertEqual(self.capture(PushNotifier()), "[push] to Alice: hi\n")

    def test_sms_only_composition_emits_only_sms_line(self):
        notifiers = [SmsNotifier()]

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            for notifier in notifiers:
                notifier.send(make_customer(), "hi")

        self.assertEqual(buffer.getvalue(), "[sms] to 555-0100: hi\n")


if __name__ == "__main__":
    unittest.main()
