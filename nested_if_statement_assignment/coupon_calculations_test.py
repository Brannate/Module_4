import unittest
from Module_4.nested_if_statement_assignment import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_under10(self):
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)

    def test_10toLT30(self):
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)

    def test_30toLT50(self):
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)

    def test_50andO(self):
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)
        self.assertEqual(coupon_calculations.calculate_price(0, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()
