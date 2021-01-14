"""
This is an example from Leetcode 344

Reverse a string in an array

s = ["h", "e", "l", "l", "o"]

rs = ["o", "l", "l", "e", "h"]

"""

import unittest

s = ["h", "e", "l", "l", "o"]


def reverse_string(s):
    """
    :param s: List of alphabet.
    :return: List of reversed string.

    Method to reverse a string in an array.
    Explanation:

    1. Assign pointers to first and last element in a list
    Therefore h -> p1 and o -> p2

    2. Increment each pointer by 1 and swap again

    3. Do this until they reach and point to the same element

    if we advance further, eventually p2 < p1.

    """

    left = 0
    right = len(s) - 1

    while left < right:
        temp = s[left]
        s[left] = s[right]
        left += 1
        s[right] = temp
        right -= 1

    return s


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        """
        Test correct string is reversed
        """
        source_string = ["h", "e", "l", "l", "o"]
        expected_string = ["o", "l", "l", "e", "h"]

        actual_string = reverse_string(source_string)

        self.assertEqual(expected_string, actual_string)


if __name__ == '__main__':
    unittest.main()
