# given an array, return indices of two numbers that they add up to a target number
# i.e. nums = [2, 7, 11 ,15] target = 9
# 2 + 7 = 9
# Thus, indice [0, 1]

# 2 approaches
# brute force and hashmap

import unittest

def bruteForceMethod(nums, target):
    for i in range(len(nums)):
        for j in range(1+i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def hashMapMethod(nums, target):
    """ hashmap uses memory so space complexity increase. """
    indice = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indice:
            return [indice[diff], i]
        indice[n] = i



class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        source_list = [2, 7, 11, 15]
        target = 9 
        expected_indice = [0, 1]

        actual_indice_brute_force = bruteForceMethod(source_list, target)
        actual_indice_hash_map = hashMapMethod(source_list, target)

        self.assertEqual(expected_indice, actual_indice_brute_force)
        self.assertEqual(expected_indice, actual_indice_hash_map)


if __name__ == '__main__':
    unittest.main()
