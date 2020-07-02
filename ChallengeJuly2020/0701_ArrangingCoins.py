__author__ = "Komal Atul Sorte"
"""
ou have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


class Solution:
    def arrangeCoins(self, n):
        index, consumed = 0, 0
        if n == 1 or n == 0:
            return n

        while consumed < n:
            index += 1
            consumed += index

        if consumed == n:
            return index
        else:
            return index - 1

    def arrangeCoinsBinarySearch(self, n):
        left, right = 1, n
        pivot = (left + right) // 2
        kk2 = None
        while left <= right:
            kk2 = pivot * (pivot + 1) // 2
            if kk2 == n:
                return pivot
            if kk2 < n:
                left = pivot + 1
            else:
                right = pivot - 1
            pivot = (left + right) // 2
        return pivot

if __name__ == '__main__':
    n = 5
    print(Solution().arrangeCoins(n))
    print(Solution().arrangeCoinsBinarySearch(n))
