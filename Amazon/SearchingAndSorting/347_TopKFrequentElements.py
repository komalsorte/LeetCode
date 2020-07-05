__author__ = "Komal Atul Sorte"
"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums, k):
        frequency = dict()
        for i in range(len(nums)):
            if nums[i] not in frequency:
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] = frequency[nums[i]] + 1

        frequency = sorted(frequency.items(), key=lambda x: x[1])
        print(frequency)

        return [val[0]]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
