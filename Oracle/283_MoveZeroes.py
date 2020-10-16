"""
LeetCode - Easy
"""
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        while index < len(nums):
            if nums[index] == 0 and index != len(nums) - 1:
                for itr in range(index + 1, len(nums)):
                    if nums[itr] != 0:
                        break
                nums[index] = nums[index] + nums[itr]
                nums[itr] = 0
            index += 1

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    # nums = [0]
    print(Solution().moveZeroes(nums))
