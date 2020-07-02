__author__ = "Komal Atul Sorte"
"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""


class Solution:
    def closestElements(self, arr, pivot, k, x):
        left, right = pivot - 1, pivot + 1

        ele = [arr[pivot]]
        while k != 1:
            if right >= len(arr) or (abs(x - arr[left]) <= abs(arr[right] - x) and left != -1):
                ele = [arr[left]] + ele
                left -= 1
                k -= 1
            elif right < len(arr):
                ele.append(arr[right])
                right += 1
                k -= 1
            if left < 0 and right >= len(arr):
                return ele
        return ele

    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - 1
        pivot = (left + right) // 2

        while left <= right:
            if arr[pivot] == x:
                return self.closestElements(arr, pivot, k, x)
            elif arr[pivot] > x:
                right = pivot - 1
            else:
                left = pivot + 1
            pivot = (left + right) // 2
        if pivot < 0:
            pivot = 0
        elif abs(arr[pivot - 1] - x) < abs(arr[pivot] - x):
            pivot -= 1
        elif abs(arr[pivot + 1] - x) < abs(arr[pivot] - x):
            pivot += 1

        return self.closestElements(arr, pivot, k, x)


if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6]
    k = 4
    x = -1
    arr = [1, 2, 3, 5, 6]
    k = 4
    x = 3
    arr = [1, 1, 1, 10, 10, 10]
    k = 1
    x = 9
    arr = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
    k = 9
    x = 4
    arr = [0, 2, 2, 3, 4, 6, 7, 8, 9, 9]
    k = 4
    x = 5
    arr = [0, 0, 0, 1, 3, 5, 6, 7, 8, 8]
    k = 2
    x = 2
    print(Solution().findClosestElements(arr, k, x))
