__author__ = "Komal Atul Sorte"
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:

    def findDifference(self, diff, numbers, i):
        left, right = 0, len(numbers) - 1
        pivot = (left + right) // 2

        while left <= right:
            if numbers[pivot] == diff and pivot != i:
                return pivot
            if diff < numbers[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
            pivot = (left + right) // 2
        return None

    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            diff = target - numbers[i]
            diff = self.findDifference(diff, numbers, i)
            if diff is not None:
                return [i + 1, diff + 1]
        return None


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    numbers = [1, 2, 3, 4, 4, 9, 56, 90]
    target = 8
    print(Solution().twoSum(numbers, target))
