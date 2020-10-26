"""
LeetCode - Easy
"""
"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        pivot = (left + right)//2

        while left <= right:
            if pivot * pivot == num:
                return True
            if pivot * pivot < num:
                left = pivot + 1
            else:
                right = pivot - 1
            pivot = (left + right)//2
        return False


if __name__ == '__main__':
    num = 17
    print(Solution().isPerfectSquare(num))
