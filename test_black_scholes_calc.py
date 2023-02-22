import unittest
from decimal import Decimal
from black_scholes_calc import get_call_price, get_put_price

class TestBlackScholesCalc(unittest.TestCase):
    def test_get_call_price(self):
        expected = Decimal('5.23')
        actual = get_call_price(Decimal('50'), Decimal('50'), Decimal('0.05'), Decimal('0.2'), Decimal('1')).quantize(Decimal('.01'))
        self.assertEqual(actual, expected)
        
    def test_get_put_price(self):
        expected = Decimal('2.79')
        actual = get_put_price(Decimal('50'), Decimal('50'), Decimal('0.05'), Decimal('0.2'), Decimal('1')).quantize(Decimal('.01'))
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()
