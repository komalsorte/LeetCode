"""
LeetCode - Easy
"""

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            return False
        else:
            # O(N) complexity
            if len(nums) == len(set(nums)):
                return False
            else:
                return True


if __name__ == '__main__':
    array = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    array = [1, 2, 3]
    print(Solution().containsDuplicate(array))
