class Solution:
    def findMaxLength(self, nums):
        count_0 = 0
        count_1 = 0
        index = 0
        while index < len(nums) - 1:

            if (nums[index] == 0 and nums[index + 1] == 1) or (nums[index] == 1 and nums[index + 1] == 0):
                count_0 += 1
                count_1 += 1
                index = index + 1
            else:
                count_0 += 0
                count_1 += 0
                index = index + 1
        if len(nums) == 2 and count_0 ==1 and count_1 ==1:
            return count_1 + count_0
        return int((count_1 + count_0) / 2)


if __name__ == '__main__':
    print(Solution().findMaxLength([0, 1]))
