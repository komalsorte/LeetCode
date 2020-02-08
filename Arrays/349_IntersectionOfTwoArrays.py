"""
Easy
"""
from typing import List


class Solution:
    def intersection(self, nums1, nums2):
        dict_int_1 = dict()
        dict_int_2 = dict()
        index_1 = 0
        index_2 = 0
        flag = True
        while flag == True:

            if index_1 != len(nums1):
                if nums1[index_1] in dict_int_1:
                    dict_int_1[nums1[index_1]] += 1
                else:
                    dict_int_1[nums1[index_1]] = 1
                index_1 += 1

            if index_2 != len(nums2):
                if nums2[index_2] in dict_int_2:
                    dict_int_2[nums2[index_2]] += 1
                else:
                    dict_int_2[nums2[index_2]] = 1
                index_2 += 1

            if index_1 == len(nums1) and index_2 == len(nums2):
                flag = False

        list_intersection = []
        for item, frequency in dict_int_1.items():
            if item in dict_int_2:
                list_intersection.append(item)
        return list_intersection


if __name__ == '__main__':
    nums1 = [3, 1, 2]
    nums2 = [1]
    print(Solution().intersection(nums1, nums2))
