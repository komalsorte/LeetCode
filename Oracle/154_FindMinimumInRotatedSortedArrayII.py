"""
LeetCode - Hard
"""
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution:
    def findMin(self, nums) -> int:
        min = float("inf")
        left, right = 0, len(nums) - 1
        pivot = (left + right) // 2

        while left <= right:
            if nums[pivot] < min:
                min = nums[pivot]
            if nums[pivot] < nums[right]:
                right = pivot - 1
            else:
                left = pivot + 1
            pivot = (left + right) // 2
        return min


if __name__ == '__main__':
    nums = [2, 2, 2, 0, 1]
    nums = [1, 3, 3]
    nums = [3, 3, 1, 3]
    print(Solution().findMin(nums))
