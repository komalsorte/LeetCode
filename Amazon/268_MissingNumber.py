__author__ = 'Komal Atul Sorte'
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""


# Complexity - O(nlogn)
# n - for loop
# log n - sort
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for num in range(len(nums)):
            if num != nums[num]:
                return num
        return len(nums)


if __name__ == '__main__':
    nums = [0, 1, 2]
    print(Solution().missingNumber(nums))
