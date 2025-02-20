import unittest

from cyb600_module6.module6 import only_odd_numbers, only_even_numbers


class Module6Tests(unittest.TestCase):
    def test_only_odd_numbers_best(self):
        test_arr = [1, 2, 3, 4, 5, 6]
        expected_arr = [1, 3, 5]
        output_arr = only_odd_numbers(test_arr)

        self.assertListEqual(expected_arr, output_arr)

    def test_only_odd_numbers_average(self):
        test_arr = [20, 40, 41, 100, 1001]
        expected_arr = [41, 1001]
        output_arr = only_odd_numbers(test_arr)

        self.assertListEqual(expected_arr, output_arr)

    def test_only_odd_numbers_worst(self):
        test_arr = "apple"
        output_arr = only_odd_numbers(test_arr)

        self.assertListEqual([], output_arr)
        
    def test_only_even_numbers_best(self):
        test_arr = [1, 2, 3, 4, 5, 6]
        expected_arr = [2, 4, 6]
        output_arr = only_even_numbers(test_arr)

        self.assertListEqual(expected_arr, output_arr)

    def test_only_even_numbers_average(self):
        test_arr = [20, 40, 41, 100, 1001]
        expected_arr = [20, 40, 100]
        output_arr = only_even_numbers(test_arr)

        self.assertListEqual(expected_arr, output_arr)

    def test_only_even_numbers_worst(self):
        test_arr = "apple"
        output_arr = only_even_numbers(test_arr)

        self.assertListEqual([], output_arr)