"""
Challenge - Find an alphabetically maximum substring from a given string.

E.g.

Given s = "bacb"

Possible substring = ["b", "ba", "bac", "bacb", "a", "ac", "acb", "c", "cb", "b"]

Alphabetically maximum substring is therefore "cb".

Complete a function that returns the maximum substring given a string input.


Sample Input:

s = "bacb"

Sample Output:

all the possible substring:
['b', 'ba', 'bac', 'bacb', 'a', 'ac', 'acb', 'c', 'cb', 'b']

"cd" is the maximum alphabetic substring

"""


def maximum_substring(s):
    """
    :param s: given string
    :return: alphabetically maximum substring given a string.

    Function explanation and approach

    list all the possible substring from a given string and find out indexes

    b     - [0:1]
    ba    - [0:2]
    bac   - [0:3]
    bacb  - [0:4]

    a     - [1:2]
    ac    - [1:3]
    acb   - [1:4]

    c     - [2:3]
    cb    - [2:4]

    b     - [3:4]

    We need two loops. First loop is range from 0-3 thus, range(4)
    Second loop range from 1-4, thus range(1, 5)

    We can use built-in Max function to retrieve the maximum substring.
    """

    substr_list = []

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr_list.append(s[i:j])

    max_substring = max(substr_list)

    # return the substring list as well to verify that correct substrings are returned

    return max_substring, substr_list
