"""
LeetCode - Easy
"""
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        intersection = set()

        if len(nums1) < len(nums2):
            nums, nums2 = nums1, nums2
        else:
            nums, nums2 = nums2, nums1


        for n in nums:
            if n in nums2:
                intersection.add(n)
        return list(intersection)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1, 3, 4]
    nums2 = [2, 2, 4, 1]
    print(Solution().intersection(nums1, nums2))
