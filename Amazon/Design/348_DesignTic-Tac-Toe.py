__author__ = "Komal Atulo Sorte"
"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.grid = []
        self.winner = 0
        self.currentToken = None
        for i in range(n):
            self.grid.append([None] * n)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.winner == 0:
            if player == 1:
                self.grid[row][col] = 'X'
                self.currentToken = 'X'
            else:
                self.grid[row][col] = '0'
                self.currentToken = '0'
            self.checkRow(row, player)
            self.checkCol(col, player)
            self.checkDiagonal(player)
            self.checkDiagonalReverse(player)
        return self.winner

    def checkRow(self, row, player):
        for col in range(len(self.grid)):
            if self.grid[row][col] != self.currentToken:
                return
        self.winner = player

    def checkCol(self, col, player):
        for row in range(len(self.grid)):
            if self.grid[row][col] != self.currentToken:
                return
        self.winner = player

    def checkDiagonal(self, player):
        n = len(self.grid)
        for i in range(n):
            if self.grid[i][i] != self.currentToken:
                return
        self.winner = player

    def checkDiagonalReverse(self, player):
        n = len(self.grid)
        for i in range(n):
            if self.grid[i][n - 1 - i] != self.currentToken:
                return
        self.winner = player


# Your TicTacToe object will be instantiated and called as such:
n = 3
obj1 = TicTacToe(n)
print(obj1.move(0, 0, 1))
print(obj1.move(0, 2, 2))
print(obj1.move(2, 2, 1))
print(obj1.move(1, 1, 2))
print(obj1.move(2, 0, 1))
print(obj1.move(1, 0, 2))
print(obj1.move(2, 1, 1))
print(obj1.move(2, 2, 2))

# ["TicTacToe","move","move","move","move","move","move","move","move","move"]
# [[3],[0,0,1],[0,2,2],[1,1,1],[2,2,2],[1,2,1],[1,0,2],[0,1,1],[2,1,2],[2,0,1]]

obj = TicTacToe(n)
print(obj.move(0, 0, 1))
print(obj.move(0, 2, 2))

print(obj.move(1, 1, 1))

print(obj.move(2, 2, 2))

print(obj.move(1, 2, 1))

print(obj.move(1, 0, 2))

print(obj.move(0, 1, 1))

print(obj.move(2, 1, 2))

print(obj.move(2, 0, 1))
