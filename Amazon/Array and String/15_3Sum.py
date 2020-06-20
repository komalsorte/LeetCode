__author__ = 'Komal Atul Sorte'
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
"""


class Solution:
    def threeSum(self, nums):
        nums.sort(reverse=True)
        b, c = 0, 0
        sum3_list = list()
        for a in range(len(nums)):
            target = -1 * nums[a]
            b = a + 1
            c = len(nums) - 1
            while b < c:
                sum = nums[b] + nums[c]
                if sum > target:
                    b += 1
                elif sum < target:
                    c -= 1
                else:
                    sum3 = [nums[a], nums[b], nums[c]]
                    if sum3 not in sum3_list:
                        sum3_list.append(sum3)
                    b += 1
                    c -= 1
        return sum3_list


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
