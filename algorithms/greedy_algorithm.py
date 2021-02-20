"""
Simple example and implementation of a Greedy Algorithm

Greedy Algorithm makes locally optimal choice at each stage to find a global optimum

Pro: simple, easy to implement
Con: Doesn't always provide the optimum

Problems solved with Greedy Algorithm satisfies 2 properties:

1. Greedy choice property: global optimum can be arrived by choosing a local optimum
2. Optimal substructure: optimal solution to the problem contains an optimal solution to sub-problems.

Greedy Algorithm doesn't reconsider its choice (difference between GA and dynamic programming).


"""

# define function that takes in amount of change as input
# return minimum number of coins to be returned
import unittest


def greedy_algorithm(n):
    """
    :param n: amount of change (in Korean won)
    :return: minimum number of coins returned (Korean won has 4 different coins, 500, 100, 50, 10)
    """

    result = 0
    # find out how many 500 won coins inside the change
    result += n // 500
    # find remainder after deducting result from the original amount
    n = n % 500
    result += n // 100
    n = n % 100
    result += n // 50
    n = n % 50
    result += n // 10

    return result


def task_assignment(n):
    """
    Takes in a list of values (correspond to number of hours required to complete a task)
    Using greedy algorithm, print pairs that results in minimum completion of tasks

    Example:

        A = [6, 3, 2, 7, 5, 5]
        if we sort [2, 3, 5, 5, 6, 7]
        if we pair smallest and largest, we get:
        [2, 7], [3, 6], [5, 5]
        so require 10 hours to complete all tasks

    * Useful information below

    n is always even number
    In Python ~ operator is a bitwise complement operator
    You invert the two's complement (bits) of a number and add 1

    2 - 0000 0010

    minus 3:
    3 - 0000 0011 -> flip 1111 1100 -> add 1 -> 1111 1101 -> -3 in bits

    if you invert 2:
    1111 1101 -> which is -3

    """
    sorted_n = sorted(n)
    for i in range(len(sorted_n)//2):
        print(sorted_n[i], sorted_n[~i])


class TestGreedyAlgorithm(unittest.TestCase):
    def test_greedy_algorithm(self):
        change = 1260
        expected_coins = 6
        actual_coins = greedy_algorithm(change)

        self.assertEqual(expected_coins, actual_coins)


if __name__ == '__main__':
    unittest.main()


# more examples to follow...


