"""
LeetCode - Medium
"""
"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        flip = False
        index, flip_index = 0, 0

        while index < len(nums):
            if nums[index] != 1 and flip is True:
                max_count = max(max_count, current_count)
                current_count = 0
                index = flip_index
                flip = False
            elif nums[index] != 1 and flip is False:
                current_count += 1
                flip = True
                flip_index = index
            else:
                current_count += 1
            index += 1
        max_count = max(max_count, current_count)
        return max_count


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
