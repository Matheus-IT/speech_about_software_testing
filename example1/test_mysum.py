import unittest
from .my_sum import sum_two_numbers


class TestMySum(unittest.TestCase):
    def test_should_sum_integers(self):
        result = sum_two_numbers(1, 2)
        self.assertEqual(result, 3)

    def test_should_sum_negatives(self):
        result = sum_two_numbers(-1, -2)
        self.assertEqual(result, -3)

    def test_should_sum_negatives_and_positives(self):
        result = sum_two_numbers(1, -2)
        self.assertEqual(result, -1)
