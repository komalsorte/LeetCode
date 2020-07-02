__author__ = "Komal Atul Sorte"
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:


Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        pivot = (left + right) // 2

        while left <= right:
            if nums[pivot] == target:
                return pivot
            if nums[left] < nums[pivot]:
                if target < nums[pivot] and target >= nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:
                if target > nums[pivot] and target <= nums[right]:
                    left = pivot + 1
                else:
                    right = pivot - 1
            pivot = (left + right) // 2
        return -1

    def getRotatedIndex(self):
        left, right = 0, len(nums) - 1
        pivot = (left + right) // 2

        while left <= right:

            if nums[pivot] > nums[left] or nums[pivot] < nums[pivot + 1]:
                left = pivot + 1
            if nums[pivot] > nums[pivot + 1]:
                break
            pivot = (left + right) // 2
        return pivot + 1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 8, 9, 0, 1, 2]
    target = 0
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    nums = [3, 1]
    target = 1
    print(Solution().search(nums=nums, target=target))
