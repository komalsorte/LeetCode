"""
LeetCode - Medium
"""
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
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
            pivot = (left + right)//2
        return min

if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    nums = [8, 7, 1, 2, 3, 4, 5, 6]
    nums = [1]
    print(Solution().findMin(nums))
