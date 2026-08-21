import subprocess
import sys
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

EXPECTED_OUTPUT = """\
>>> Checkout a simple order
[payment] Charging card 4111 1111 1111 1111 819.99
[email] to alice@example.com: Order 101 total $819.99 (paid_by_credit_card:819.99)
[sms] to 555-0100: Order 101 total $819.99 (paid_by_credit_card:819.99)
--- Receipt for order 101 ---
  Laptop               x1  $999.99
  Mouse                x1  $25.00
  Subtotal    $1024.99
  Discount   -$205.00
  Shipping    $0.00
  TOTAL       $819.99
  Payment     paid_by_credit_card:819.99

>>> Checkout a bundle of two orders
[payment] Charging card 4111 1111 1111 1111 955.99
[email] to alice@example.com: Order 103 total $955.99 (paid_by_credit_card:955.99)
[sms] to 555-0100: Order 103 total $955.99 (paid_by_credit_card:955.99)
--- Receipt for order 103 ---
  Laptop               x1  $999.99
  Mouse                x1  $25.00
  Clean Code           x2  $90.00
  Pragmatic Programmer x2  $80.00
  Subtotal    $1194.99
  Discount   -$239.00
  Shipping    $0.00
  TOTAL       $955.99
  Payment     paid_by_credit_card:955.99
"""


class GoldenDemoTests(unittest.TestCase):
    def test_full_demo_output_matches_expected(self):
        result = subprocess.run(
            [sys.executable, "-B", "-m", "store.main"],
            cwd=str(PROJECT_DIR),
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(result.stdout.replace("\r\n", "\n"), EXPECTED_OUTPUT)


if __name__ == "__main__":
    unittest.main()
