import unittest

from .prime import is_prime


class Tests(unittest.TestCase):
    def test_should_be_truthy_if_number_is_prime(self):
        prime_number = 2
        self.assertTrue(is_prime(prime_number))

    def test_should_be_falsy_for_number_that_is_not_prime(self):
        not_prime_number = 8
        self.assertFalse(is_prime(not_prime_number))

    def test_should_be_falsy_if_negative(self):
        negative = -1
        self.assertFalse(is_prime(negative))


if __name__ == "__main__":
    unittest.main()
