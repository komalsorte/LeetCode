"""
Easy
"""
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A_squared = []
        for index in range(len(A)):
            mul = A[index] * A[index]
            A_squared.append(mul)
        A_squared.sort()
        return A_squared


if __name__ == '__main__':
    print(Solution().sortedSquares([-7,-3,2,3,11]))