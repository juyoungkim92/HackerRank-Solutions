"""
HackerRank Challenge: https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters.
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.

E.g.

Input s = "AAABBB"
output = 4

"""


def alternating_characters(s):
    """
    :param s: input string "AAABBB" etc.
    :return: Integer denoting how many deletions must be performed.

    Function explanation:

    For a given string, we need to know if a consecutive letter is the same letter or not.
    If the next letter is same, we should delete such that AAB becomes AB. Following this logic,
    We can start the string iteration from range(1, len(s)) and use i-1 to count from 0th index.

    """

    del_count = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            del_count += 1

    return del_count
