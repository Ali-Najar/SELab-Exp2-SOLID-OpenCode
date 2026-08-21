import unittest

from store.models import Customer, Order
from store.storage import MySqlDatabase


class MySqlDatabaseTests(unittest.TestCase):
    def test_save_then_load_roundtrip(self):
        db = MySqlDatabase()
        order = Order(id=7, customer=Customer(id=1, name="A", email="a@x.com"))

        db.save_order(order)

        self.assertIs(db.load_order(7), order)

    def test_load_missing_returns_none(self):
        db = MySqlDatabase()

        self.assertIsNone(db.load_order(999))

    def test_save_same_id_replaces_entry(self):
        db = MySqlDatabase()
        first = Order(id=7, customer=Customer(id=1, name="A", email="a@x.com"))
        second = Order(id=7, customer=Customer(id=1, name="A", email="a@x.com"))

        db.save_order(first)
        db.save_order(second)

        self.assertIs(db.load_order(7), second)


if __name__ == "__main__":
    unittest.main()
