"""
LeetCode - Medium
"""


class Solution:
    def findDuplicates(self, nums):
        dict_nums = dict()
        dict_nums_res = dict()
        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
                dict_nums_res[num] = num
            else:
                dict_nums[num] = 1
        return list(dict_nums_res)





if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(nums))