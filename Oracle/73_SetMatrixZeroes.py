"""
LeetCode - Medium
"""
"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_set = set()
        col_set = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0

        print(matrix)


if __name__ == '__main__':
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]

    matrix1 = [[0, 1, 2, 0],
               [3, 4, 5, 2],
               [1, 3, 1, 5]]

    print(Solution().setZeroes(matrix1))
