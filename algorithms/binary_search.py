"""
Example implementation of a binary search.

Time complexity of binary search is O(log n)

Binary search algorithm works on sorted list.

"""

import time


def time_it(func):
    """
    Decorator for measuring time. Decorators in Python:

    @time_it
    def some_function() is same as

    some_function = time_it(some_function)
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {str((end-start)*1000)} milliseconds.")
        return result

    return wrapper


@time_it
def linear_search(num_list, num_find):
    """ find index using for loop iteration. O(n) """
    for ind, element in enumerate(num_list):
        if element == num_find:
            return ind


@time_it
def binary_search(num_list, num_find):
    """ find index using binary search. O(log n) """
    left_index = 0
    right_index = len(num_list) - 1

    # iterate until left index is <= right index
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2  # double slash keeps the whole number
        mid_number = num_list[mid_index]

        if mid_number == num_find:
            return mid_index

        # you reset the left index by discarding everything from left to mid number thus
        # left index is mid_index + 1
        if mid_number < num_find:
            left_index = mid_index + 1

        # if mid number is bigger than num find
        # keep left numbers and discard everything from right of mid number thus, right index is mid - 1 index
        else:
            right_index = mid_index - 1

    # if not find anything return -1 but here we want to return the left_index when left_index == right_index
    return left_index


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    """
    Recursive binary search. Search in the boundary of left and right indices.
    In recursion you don't have loops
    """
    if right_index < left_index:
        return -1  # we don't find element.

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    # Call function again recursively
    # return mid_index
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 67432

    # Test speed by making large list
    # numbers_list = [i for i in range(1000001)]
    # number_to_find = 3213

    # linear search
    linear_search_index = linear_search(numbers_list, number_to_find)  # takes 71 milli seconds
    print(f"Number found at index {linear_search_index} using linear search.")

    # binary search
    binary_search_index = binary_search(numbers_list, number_to_find)  # takes 0.01 milli seconds
    print(f"Number found at index {binary_search_index} using binary search.")

    # recursive binary search
    recursive_bs_index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index {recursive_bs_index} using recursive binary search.")
