"""
Easy
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        dictOfnums = {i: 0 for i in nums}
        length = len(nums)
        nums = []
        i = 0
        while i <= length:
            if i in dictOfnums or i == 0:
                pass
            else:
                nums.append(i)
            i += 1
        return nums


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([1, 1]))
