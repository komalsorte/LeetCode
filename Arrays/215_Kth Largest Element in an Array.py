"""
Medium
"""
class Solution:
    def findKthLargest(self, nums, k):
        target = 0
        max = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        print(nums)
        return nums[k-1]
if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))