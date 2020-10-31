"""
LeetCode - Medium
"""
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        board = board[0]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.dfs(row, col, word, 0, board):
                        return True
        return False

    def dfs(self, row, col, word, index, board):
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[index]:
            if index + 1 == len(word):
                return True
            if board[row][col].isupper():
                board[row][col] = board[row][col].lower()
            else:
                board[row][col] = board[row][col].upper()

            # call up
            up = self.dfs(row - 1, col, word, index + 1, board)
            # call down
            down = self.dfs(row + 1, col, word, index + 1, board)
            # call left
            left = self.dfs(row, col - 1, word, index + 1, board)
            # call right
            right = self.dfs(row, col + 1, word, index + 1, board)

            if board[row][col].isupper():
                board[row][col] = board[row][col].lower()
            else:
                board[row][col] = board[row][col].upper()
            return up or down or left or right
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]],
    word = "ABCCED"
    word = "SEE"
    word = "ABCB"
    print(Solution().exist(board, word))
