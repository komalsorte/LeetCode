"""
LeetCode - Easy
"""
"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        head = 0
        while True:
            if A == B:
                return True
            else:
                A = A[1: len(A)] + A[0]
                if head == 0:
                    head = len(A) - 1
                else:
                    head -= 1
            if head == 0:
                break
        return False


if __name__ == '__main__':
    A = 'abcde'
    B = 'cdeab'

    A = 'abcde'
    B = 'abced'

    print(Solution().rotateString(A, B))
