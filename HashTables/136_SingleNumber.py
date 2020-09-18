"""
LeetCode - Easy
"""

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    mapCount = dict()

    def singleNumber(self, nums):
        for n in nums:
            if n in self.mapCount.keys():
                del self.mapCount[n]
            else:
                self.mapCount[n] = 1

        return self.mapCount.popitem()[0]


if __name__ == '__main__':
    nums = [2, 3, 4, 1,1, 3, 4]
    print(Solution().singleNumber(nums))
