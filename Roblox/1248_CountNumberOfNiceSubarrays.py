"""
LeetCode - Medium
"""

"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

"""
EXCEEDS TIME LIMIT
"""
class Solution:
    def numberOfSubarrays(self, nums, k):
        current, index, limit = 0, 0, 0
        niceArrays = list()
        while current < len(nums):
            if limit < k and nums[index] % 2 != 0:
                limit += 1
                index += 1
                if limit == k:
                    niceArrays.append(nums[current: index])
            elif (nums[index] % 2 != 0 and limit == k):
                current += 1
                index = current
                limit = 0
            elif limit == k:
                index += 1
                niceArrays.append(nums[current: index])
            else:
                index += 1
            if index == len(nums):
                current += 1
                index = current
                limit = 0
        return len(niceArrays)


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 0, 1]
    k = 3
    print(Solution().numberOfSubarrays(nums, k))
