"""
LeetCode - Medium
"""
"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""


class Solution:
    def __init__(self):
        self.grid = []
        self.islands = 0
    def numIslands(self, grid) -> int:
        self.grid = grid

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    self.dfs(row, col)
                    self.islands += 1

        return self.islands

    def dfs(self, row, col):
        if len(self.grid) > row > -1 and len(self.grid[0]) > col > -1 and self.grid[row][col] == '1':
            self.grid[row][col] = "#"
            # go up
            self.dfs(row - 1, col)
            # go down
            self.dfs(row + 1, col)
            # go left
            self.dfs(row, col - 1)
            # go right
            self.dfs(row, col + 1)


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))
