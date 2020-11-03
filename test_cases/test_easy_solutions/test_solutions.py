import unittest
from challenges.easy.sales_by_match import sales_by_match
from challenges.easy.counting_valleys import counting_valleys
from challenges.easy.alphabetically_maximum_substring import maximum_substring
from challenges.easy.alternating_characters import alternating_characters
from challenges.easy.arrays_left_rotation import array_rotation_left_method_1, array_rotation_left_method_2


class TestEasySolutions(unittest.TestCase):
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

    def test_counting_valleys(self):
        """
        Test that correct number of valleys were traversed
        """
        source_string = "UDDDUDUU"
        expected_valley_count = 1

        actual_valleys_count = counting_valleys(source_string)

        self.assertEqual(expected_valley_count, actual_valleys_count)

    def test_maximum_substring(self):
        """
        Test correct maximum substring is returned
        """
        source_string = "bacb"
        expected_substrings = ['b', 'ba', 'bac', 'bacb', 'a', 'ac', 'acb', 'c', 'cb', 'b']
        expected_max_substring = "cb"

        max_substr, substr_array = maximum_substring(source_string)

        self.assertEqual(expected_max_substring, max_substr)
        self.assertListEqual(expected_substrings, substr_array)

    def test_alternating_characters(self):
        """
        Test correct maximum substring is returned
        """
        source_string = "AAABBB"
        expected_deletion_count = 4

        actual_count = alternating_characters(source_string)

        self.assertEqual(expected_deletion_count, actual_count)

    def test_left_rotation_method_1(self):
        """
        Test correct array is returned after rotation using time complexity of O(n) with no constraints
        """
        source_array = [1, 2, 3, 4, 5]
        rotation_count = 6
        expected_array = [2, 3, 4, 5, 1]

        actual_array = array_rotation_left_method_1(source_array, rotation_count)

        self.assertEqual(expected_array, actual_array)

    def test_left_rotation_method_2(self):
        """
        Test correct array is returned after rotation using time complexity of O(1) with constraints
        """
        source_array = [1, 2, 3, 4, 5]
        rotation_count = 4
        expected_array = [5, 1, 2, 3, 4]

        actual_array = array_rotation_left_method_2(source_array, rotation_count)

        self.assertEqual(expected_array, actual_array)


if __name__ == '__main__':
    unittest.main()
