__author__ = 'Komal Atul Sorte'
"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums):

        left = [1] * len(nums)
        right = [1] * len(nums)
        output = [1] * len(nums)
        for n in range(len(nums)):
            if n == 0:
                left[n] = nums[n]
            else:
                left[n] = left[n - 1] * nums[n]
        for n in range(len(nums) - 1, -1, -1):
            if n == len(nums) - 1:
                right[n] = nums[n]
            else:
                right[n] = right[n + 1] * nums[n]
        print(left)
        print(right)
        # Exceeds time limit -  O(n2)
        # output = [1] * len(nums)
        # for n in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != n:
        #             output[n] = nums[j] * output[n]
        # return output
        for n in range(len(nums)):
            if n == 0:
                output[n] = right[n + 1]
            elif n == len(nums) - 1:
                output[n] = left[n - 1]
            else:
                output[n] = right[n + 1] * left[n - 1]
        return output


if __name__ == '__main__':
    num = [1, 2, 3, 4, 0]
    print(Solution().productExceptSelf(num))
