"""
LeetCode - Medium
"""
from collections import defaultdict, Counter

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
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):

        map = defaultdict()
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        return heapq.nlargest(k, map.keys(), key=map.get)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6]
    k = 2
    print(Solution().topKFrequent(nums, k))
