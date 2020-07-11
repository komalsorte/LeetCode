__author__ = "Komal Atul Sorte"
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution1:
    # 200 / 202 test cases passed.
    def maxSubArray1(self, nums):
        if len(nums) == 1:
            return nums[0]
        start, end = 0, 0
        maxSum = float('-inf')
        # maxSumArray = list()
        currentSum = 0
        while start != len(nums):
            currentSum += nums[end]
            if currentSum > maxSum:
                maxSum = currentSum
                # maxSumArray = nums[start: end + 1]
            end += 1
            if end == len(nums):
                start += 1
                end = start
                currentSum = 0
        return maxSum

    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)

        return max_sum


class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2, 1]
    print(Solution().maxSubArray(nums))
