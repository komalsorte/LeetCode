"""
LeetCode - Medium
"""
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""


class Solution:
    def findWords(self, board, words):
        found = []
        for w in words:
            if self.exist(board, w):
                found.append(w)
        return found

    def exist(self, board, word: str) -> bool:
        # board = board[0]
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
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords(board, words))
