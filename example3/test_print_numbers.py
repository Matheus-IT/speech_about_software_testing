import unittest
from unittest.mock import patch, call
from .print_numbers import print_ten_numbers


class TestPrintNumbers(unittest.TestCase):
    def test_should_print_ten_times(self):
        with patch("builtins.print") as mock_print:
            print_ten_numbers()
            self.assertEqual(mock_print.call_count, 10)

    @patch("builtins.print")
    def test_should_start_printing_from_zero(self, mock_print):
        print_ten_numbers()
        self.assertEqual(mock_print.mock_calls[0], call(0))


if __name__ == "__main__":
    unittest.main()
