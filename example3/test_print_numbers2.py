import unittest
from unittest.mock import patch, call
from .print_numbers2 import print_ten_numbers
from .monkey_patched_presenter import MonkeyPatchedPresenter


class TestPrintNumbers(unittest.TestCase):
    def test_should_print_ten_times(self):
        presenter = MonkeyPatchedPresenter()
        print_ten_numbers(presenter)
        self.assertEqual(presenter.called, 10)


if __name__ == '__main__':
    unittest.main()
