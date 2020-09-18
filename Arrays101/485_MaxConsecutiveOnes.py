"""
LeetCode - Easy
"""

"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0

        for num in nums:
            if num != 1:
                max_count = max(max_count, current_count)
                current_count = 0
            else:
                current_count += 1
        max_count = max(max_count, current_count)
        return max_count


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
