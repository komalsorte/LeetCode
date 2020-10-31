"""
LeetCode - Medium
"""


class Solution:

    def threeSum(self, nums):
        triplets = set()
        triplets_list = list()
        nums.sort()  # -3 -1 -1 0 2
        n = 0
        while n < len(nums):
            if nums[n] > 0:
                break
            self.findZero(n, triplets, nums)
            n = n + 1

        for t in triplets:
            triplets_list.append(list(t))
        return triplets_list

    def findZero(self, n, triplets, nums):
        left = n + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right] + nums[n]
            if sum == 0 and (nums[n], nums[left], nums[right]) not in triplets:
                triplets.add((nums[n], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]
    print(Solution().threeSum(nums))
