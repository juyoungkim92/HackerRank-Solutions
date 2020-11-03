"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

A left rotation operation on an array shifts each of the array's elements  unit to the left.
For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.

For example, input array: [1,2,3,4,5]
left rotation number: 4

final output should be: [5,1,2,3,4]

1st round: [2,3,4,5,1]
2nd round: [3,4,5,1,2]
3rd round: [4,5,1,2,3]
4th round: [5,1,2,3,4]

"""


def array_rotation_left_method_1(array, d):
    """
    :param array: input array
    :param d: number of rotation integer
    :return: final array

    Method 1.

    Disadvantage:
    1. time complexity to O(n) if d increases
    2. time complexity still O(n) since pop() deletes and shift everything i.e. there is a shift cost

    Advantage:
    1. no constraints required i.e. d <= n

    """

    for _ in range(d):
        temp = array.pop(0)
        array.append(temp)

    return array


def array_rotation_left_method_2(array, d):
    """
    :param array: input array
    :param d: number of rotation integer
    :return: final array

    Method 2. using Python slicing.

    Disadvantage:
    1. cannot ignore constraints of n <= d

    Advantage:
    1. time complexity is O(1) because access element in array using an index.
    This is possible because in array, logical memory and physical memory address is the same.

    """

    return array[d:] + array[:d]
