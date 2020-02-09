"""
Medium
"""
class Solution:
    def search(self, nums, target):
        for index_1 in range(len(nums)):
            if target == nums[index_1]:
                return index_1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))
