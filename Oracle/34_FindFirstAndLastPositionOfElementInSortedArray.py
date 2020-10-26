"""
LeetCode - Medium
"""
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0, 0]
            else:
                return [-1, -1]

        left = 0
        right = len(nums) - 1
        pivot = (left + right) // 2

        while left < right:
            if nums[pivot] == target:
                right = pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
            pivot = (left + right) // 2
        if nums[pivot] != target:
            return [-1, -1]
        left_extreme = pivot
        left = pivot
        right = len(nums) - 1
        pivot = (left + right) // 2
        while left < right:
            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] == target:
                left = pivot + 1
            pivot = (left + right) // 2
        right_extreme = pivot
        return [left_extreme, right_extreme - 1]

if __name__ == '__main__':
    print(Solution().searchRange(nums=[5, 7, 7, 7, 7, 7, 7, 8, 8, 8, 10], target=7))
    print(Solution().searchRange(nums=[1], target=1))
