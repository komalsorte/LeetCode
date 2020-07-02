__author__ = "Komal Atul Sorte"
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.
"""


class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) -1
        pivot = (left + right) // 2

        while left < right:
            if nums[pivot] >= nums[pivot - 1] and nums[pivot] >= nums[pivot + 1]:
                return pivot
            if nums[pivot] < nums[pivot + 1]:
                left = pivot + 1
            else:
                right = pivot - 1
            pivot = (left + right) // 2
        return pivot
        # if len(nums) == 1:
        #     return 0
        # pivot = (0 + len(nums) - 1) // 2
        # left, right = pivot - 1, pivot + 1
        #
        # while left <= right:
        #     if nums[pivot] >= nums[left] and nums[pivot] >= nums[right]:
        #         return pivot
        #     if nums[pivot] < nums[right]:
        #         left = pivot
        #         pivot = pivot + 1
        #         if pivot == len(nums) - 1:
        #             right = pivot
        #         else:
        #             right = pivot + 1
        #     if nums[pivot] < nums[left]:
        #         right = pivot
        #         pivot = pivot - 1
        #         if pivot == 0:
        #             left = pivot
        #         else:
        #             left = pivot - 1


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    nums = [1, 1, 2, 1, 1]
    nums = [1, 6, 5, 3, 0, 6, 4]
    nums = [1]
    nums = [1, 2]
    nums = [0,1,2,3,4,5]
    print(Solution().findPeakElement(nums=nums))
