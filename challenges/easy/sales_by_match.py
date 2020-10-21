"""
HackerRank challenge link: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Sales by Match

Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . There is one pair of color  and one of color .
There are three odd socks left, one of each color. The number of pairs is .

Function Description

It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock


Sample Input:

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output:

3

"""


def sales_by_match(arr):
    """
    :param arr: list of matching socks
    :return: integer of matching pair

    Function explanation:

    We can first count the occurrence of the individual socks in a list.
    For this we can first get the unique items in a list and count each unique items in a list.
    Once counted, we can do an integer division to get a number of pairs.
    We can increment the pair we initialised in the beginning by the number we got and return the final pairs.

    """
    pairs = 0

    for i in set(arr):
        pairs += arr.count(i) // 2  # integer division

    return pairs
