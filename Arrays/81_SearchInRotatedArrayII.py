"""
Medium
"""
class Solution:
    def search(self, nums, target):
        for num in nums:
            if target == num:
                return True
        return False

if __name__ == '__main__':
    nums = [2,5,6,0,0,1,2]
    target = 3
    print(Solution().search(nums, target))
