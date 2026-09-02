import unittest

from calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_and_positive_number(self):
        self.assertEqual(add(-1, 4), 3)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply_numbers(self):
        self.assertEqual(multiply(3, 5), 15)


if __name__ == "__main__":
    unittest.main()