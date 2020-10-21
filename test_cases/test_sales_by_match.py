import unittest
from challenges.easy.sales_by_match import sales_by_match


class TestSalesByMatch(unittest.TestCase):
    """
    Test case
    """
    def test_sale_by_match(self):
        """
        Test that correct number of pairs are returned from the function
        """
        source_array_1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        source_array_2 = [1, 1, 1, 1, 3, 1, 5, 2, 2, 2, 5, 2, 6, 7]
        expected_pair_1 = 3
        expected_pair_2 = 5
        actual_pairs_1 = sales_by_match(source_array_1)
        actual_pairs_2 = sales_by_match(source_array_2)

        self.assertEqual(expected_pair_1, actual_pairs_1)
        self.assertEqual(expected_pair_2, actual_pairs_2)
