"""
LeetCode - Easy
"""
"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

"""


class Solution:
    def __init__(self):
        self.turn = "Alice"
    def divisorGame(self, N):
        if N == 1 and self.turn == "Alice":
            return False
        elif N == 1 and self.turn == "Bob":
            return True
        else:
            if self.turn == "Alice":
                self.turn = "Bob"
            else:
                self.turn = "Alice"
            return self.divisorGame(N-1)

if __name__ == '__main__':
    print(Solution().divisorGame(3))

