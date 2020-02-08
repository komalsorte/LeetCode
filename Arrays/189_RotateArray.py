"""
Easy
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            last = nums[len(nums)-1]
            nums = nums[:len(nums)-1]
            nums = [last] + nums
        return nums

if __name__ == '__main__':
    print(Solution().rotate([-1,-100,3,99], 2))