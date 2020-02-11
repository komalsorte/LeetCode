"""
LeetCode - Easy
"""
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # convert integer to string
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count = count + 1
        return count


if __name__ == '__main__':
    Solution().findNumbers([12, 345, 2, 6, 7896])
