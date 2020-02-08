"""
Easy
"""
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        dict_int = dict()
        index_1 = 0
        index_2 = 0
        index_3 = 0
        while index_1 < len(arr1) and index_2 < len(arr2) and index_3 < len(arr3):

            if index_1 != len(arr1):
                if arr1[index_1] in dict_int:
                    dict_int[arr1[index_1]] += 1
                else:
                    dict_int[arr1[index_1]] = 1
                index_1 += 1
            if index_2 != len(arr2):
                if arr2[index_2] in dict_int:
                    dict_int[arr2[index_2]] += 1
                else:
                    dict_int[arr2[index_2]] = 1
                index_2 += 1
            if index_3 != len(arr3):
                if arr3[index_3] in dict_int:
                    dict_int[arr3[index_3]] += 1
                else:
                    dict_int[arr3[index_3]] = 1
                index_3 += 1

        list_intersection = []
        for item, frequency in dict_int.items():
            if frequency >= 3:
                list_intersection.append(item)
        return list_intersection



if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(Solution().arraysIntersection(arr1, arr2, arr3))
