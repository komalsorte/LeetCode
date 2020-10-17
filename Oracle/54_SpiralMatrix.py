"""
LeetCode - Medium
"""
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        spiralOrderList = list()
        topSpiral = 0
        if len(matrix) == 0:
            return []
        rightSpiral = len(matrix[0]) - 1
        bottomSpiral = len(matrix) - 1
        leftSpiral = 0
        size = len(matrix[0]) * len(matrix)

        while leftSpiral <= rightSpiral and bottomSpiral >= topSpiral:
            for col in range(leftSpiral, rightSpiral + 1):
                spiralOrderList.append(matrix[topSpiral][col])

            if len(spiralOrderList) == size:
                break

            for row in range(topSpiral + 1, bottomSpiral + 1):
                spiralOrderList.append(matrix[row][rightSpiral])

            if len(spiralOrderList) == size:
                break

            for col in range(rightSpiral - 1, leftSpiral - 1, -1):
                spiralOrderList.append(matrix[bottomSpiral][col])

            if len(spiralOrderList) == size:
                break

            for row in range(bottomSpiral - 1, topSpiral, -1):
                spiralOrderList.append(matrix[row][leftSpiral])

            if len(spiralOrderList) == size:
                break

            topSpiral += 1
            rightSpiral -= 1
            bottomSpiral -= 1
            leftSpiral += 1

        return (spiralOrderList)

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]

    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print(Solution().spiralOrder(matrix2))
