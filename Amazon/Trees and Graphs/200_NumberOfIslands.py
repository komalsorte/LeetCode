__author__ = "Komal Atul Sorte"
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid):
        countIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    countIslands += 1
                    self.dfs(r, c, grid)
                else:
                    grid[r][c] = "#"
        return countIslands

    def dfs(self, r, c, grid):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        self.dfs(r - 1, c, grid)
        self.dfs(r + 1, c, grid)
        self.dfs(r, c - 1, grid)
        self.dfs(r, c + 1, grid)


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]

    print(Solution().numIslands(grid=grid))
