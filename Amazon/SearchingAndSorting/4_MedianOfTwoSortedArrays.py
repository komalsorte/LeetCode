__author__ = "Komal Atul Sorte"
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    # Complexity = O(m + n)
    def findMedianSortedArrays(self, nums1, nums2):
        index_num1, index_num2 = 0, 0
        nums = []
        median = None

        while index_num1 < len(nums1) and index_num2 < len(nums2):
            if nums1[index_num1] < nums2[index_num2]:
                nums.append(nums1[index_num1])
                index_num1 += 1
            elif nums1[index_num1] > nums2[index_num2]:
                nums.append(nums2[index_num2])
                index_num2 += 1
            else:
                nums.append(nums1[index_num1])
                nums.append(nums2[index_num2])
                index_num1 += 1
                index_num2 += 1
        if index_num1 < len(nums1):
            nums = nums + nums1[index_num1: len(nums1)]
        elif index_num2 < len(nums2):
            nums = nums + nums2[index_num2: len(nums2)]

        if len(nums) % 2 == 0:
            median = nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]
            median = median / 2
        else:
            median = nums[int(len(nums) / 2)]
        return median


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
