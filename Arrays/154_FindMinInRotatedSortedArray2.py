"""
Hard


DOUBT: ANOTHER WAY
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictOfNums = {i: 0 for i in nums}
        return(min(dictOfNums))

if __name__ == '__main__':
    print(Solution().findMin([2,2,2,0,8]))