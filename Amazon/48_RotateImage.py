__author__ = 'Komal Atul Sorte'
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if r >= c:
                    temp = matrix[r][c]
                    matrix[r][c] = matrix[c][r]
                    matrix[c][r] = temp
                else:
                    break
        for r in range(len(matrix)):
            matrix[r].reverse()
        return matrix


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print(Solution().rotate(matrix))
