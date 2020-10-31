__author__ = "Komal Atul Sorte"
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:

    def getLow(self, start, end, nums, target):
        left, right = start, end
        low = -1
        pivot = (left + right) // 2

        while left <= right:
            if target == nums[pivot]:
                right = pivot - 1
                if low > pivot or low == -1:
                    low = pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
            pivot = (left + right) // 2
        return low

    def getHigh(self, end, start, nums, target):
        left, right = start, end
        pivot = (left + right) // 2
        high = -1
        while left <= right:
            if target == nums[pivot]:
                left = pivot + 1
                if high == -1 or high < pivot:
                    high = pivot
            elif target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
            pivot = (left + right) // 2
        return high

    def searchRange(self, nums, target: int):
        if nums == []:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        mid = int((left + right) / 2)
        low, high = -1, -1

        while left <= right:
            if nums[mid] == target:
                # search low
                low = self.getLow(left, mid, nums, target)

                # search high
                high = self.getHigh(right, mid, nums, target)

                if mid < low and low != -1:
                    low = mid
                if high < mid and high != -1:
                    high = mid
                return [low, high]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = int((left + right) / 2)

        return [low, high]


if __name__ == '__main__':
    nums = [2, 3, 4, 5, 5, 5, 5, 7, 7, 8, 8, 10]
    target = 5
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    print(Solution().searchRange(nums, target))
