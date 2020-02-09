"""
Hard
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        for num in nums:
            if min > num:
                min = num
        return min

if __name__ == '__main__':
    print(Solution().findMin([2,2,2,0,8]))