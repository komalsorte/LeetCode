"""
LeetCode - Easy
"""
"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        distance_tracker = {n: '#' for n in set(nums)}
        print(distance_tracker)

        for index, n in enumerate(nums):
            if distance_tracker[n] == '#':
                distance_tracker[n] = index
            else:
                if abs(distance_tracker[n] - index) <= k:
                    return True
                else:
                    distance_tracker[n] = index


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 3]
    k = 2
    print(Solution().containsNearbyDuplicate(nums, k))

