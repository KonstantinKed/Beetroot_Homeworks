import unittest
from Task16_3 import Product, ProductStore

class ProductStoreTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.p1 = Product('Sport', 'Football T-Shirt', 100)
        self.p2 = Product('Mobile', 'iPhone', 1000)
        self.store = ProductStore()

    def test_add(self):
        self.store.add(self.p1, 20)
        self.assertIn(self.p1, self.store.product_store) # check if products add to list
        self.assertEqual(self.store.product_store[0].price, 130) # check if price is raised to premium

    def test_set_discount(self):
        self.store.add(self.p1, 20)
        self.store.add(self.p2, 10)
        self.store.set_discount(self.p1.name, 10)
        self.assertEqual(self.store.product_store[0].price, 117, "check if discount works")

        with self.assertRaises(ValueError):
            self.store.set_discount(self.p1.name, 100)  # not working!!!!

    def test_sell_product(self):
        self.store.add(self.p1, 10)
        self.store.add(self.p2, 10)
        self.store.sell_product('iPhone', 1)
        self.assertEqual(self.store.product_store[1].amount, 9) # check if amount reduce after selling

        with self.assertRaises(ValueError):
            self.store.sell_product(self.p1.name, 11)

    def test_income(self):
        self.store.add(self.p2, 10)
        self.store.sell_product('iPhone', 1)
        self.assertTrue(self.store.income)
        self.assertEqual(self.store.income, 1300, "income after selling")

    def test_get_all_product(self):
        self.store.add(self.p1, 10)
        self.store.add(self.p2, 10)
        self.assertIn(self.p1, self.store.product_store)
        self.assertIn(self.p2, self.store.product_store)

if __name__ == '__main__':
    unittest.main()