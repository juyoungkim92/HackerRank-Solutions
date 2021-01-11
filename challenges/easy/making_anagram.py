"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/submissions/code/195214331?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings.

a = "cde"
b = "dcf"

Delete e from a
Delete f from b
the remaining strings are cd and dc which are anagrams

"""

# useful Python Counter to count elements in a string
from collections import Counter


def make_anagram(string_a, string_b):
    """
    Function to check how many minimum deletions must happen to create an anagram between two strings
    :param string_a:
    :param string_b:

    Explanation:

    First count number of each letter in the given strings using Counter

    a = "aabyye"
    b = "bda"

    dict_a = { a: 2, b: 1, y: 2, e: 1}
    dict_b = { b: 1, d: 1, a: 1}

    Do the diffs between two both sides

    a - b = { a: 1, b: 0, y: 2, e: 1}
    b - a = { b: 0, d: 1, a: 0}

    Any positive integers above will be the deletions required
    Thus do the sum of all the values above with sum(diff.values()) + sum(diff.values())

    :return:
    """
    count_a = Counter(string_a)
    count_b = Counter(string_b)
    diff_count_a = count_a - count_b
    diff_count_b = count_b - count_a

    return sum(diff_count_a.values()) + sum(diff_count_b.values())
