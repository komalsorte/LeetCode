"""
LeetCode - Medium
"""
"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from collections import deque


class Solution:
    def __init__(self):
        self.gate = 0
        self.walls = -1
        self.INF = 2 ** 31 - 1
        self.queue = deque()

    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == self.gate:
                    self.queue.append([row, col])

        while len(self.queue) != 0:
            current = self.queue.popleft()
            current_row, current_col = current[0], current[1]
            # go up
            self.goDirection(current_row - 1, current_col, rooms[current_row][current_col] + 1, rooms)
            # go down
            self.goDirection(current_row + 1, current_col, rooms[current_row][current_col] + 1, rooms)
            # go left
            self.goDirection(current_row, current_col - 1, rooms[current_row][current_col] + 1, rooms)
            # go right
            self.goDirection(current_row, current_col + 1, rooms[current_row][current_col] + 1, rooms)

        return rooms

    def goDirection(self, row, col, value, rooms):

        if len(rooms) > row > -1 and \
                len(rooms[0]) > col > -1 and \
                rooms[row][col] != self.gate and rooms[row][col] != self.walls:
            if rooms[row][col] > value:
                rooms[row][col] = value
                self.queue.append([row, col])


if __name__ == '__main__':
    INF = 2 ** 31 - 1
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, -1, INF]

    ]

    print(Solution().wallsAndGates(rooms))
