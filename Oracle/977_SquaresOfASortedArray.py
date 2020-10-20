"""
LeetCode - Easy
"""
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

"""


class Solution:
    def sortedSquares(self, A):
        positive, negative = len(A), -1
        squares = []
        for i in range(len(A)):
            if A[i] >= 0:
                positive = i
                break

        negative = positive - 1
        while positive < len(A) and negative > -1:
            if abs(A[positive]) < abs(A[negative]):
                squares.append(A[positive] * A[positive])
                positive += 1
            elif abs(A[positive]) > abs(A[negative]):
                squares.append(A[negative] * A[negative])
                negative -= 1
            else:
                squares.append(A[positive] * A[positive])
                squares.append(A[negative] * A[negative])
                positive += 1
                negative -= 1

        while positive < len(A):
            squares.append(A[positive] * A[positive])
            positive += 1
        while negative > -1:
            squares.append(A[negative] * A[negative])
            negative -= 1

        return squares


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    A = [-1]
    print(Solution().sortedSquares(A))
