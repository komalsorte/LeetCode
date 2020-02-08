class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        dict_int = dict()
        for a1 in arr1:
            if a1 in dict_int:
                dict_int[a1] += 1
            else:
                dict_int[a1] = 1
        for a2 in arr2:
            if a2 in dict_int:
                dict_int[a2] += 1
            else:
                dict_int[a2] = 1
        for a3 in arr3:
            if a1 in dict_int:
                dict_int[a3] += 1
            else:
                dict_int[a3] = 1


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(Solution().arraysIntersection(arr1, arr2,arr3))