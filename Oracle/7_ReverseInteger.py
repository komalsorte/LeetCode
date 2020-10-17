"""
LeetCode - Easy
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        reverseInt, sign = 0, 1

        if x < pow(-2, 31) or x >= pow(2, 31):
            return 0

        if x < 0:
            sign = -1

        while x != 0:
            reverseInt = reverseInt * 10 + abs(x) % 10
            x = abs(int(x / 10))
            if reverseInt < pow(-2, 31) or reverseInt >= pow(2, 31):
                return 0

        return sign * reverseInt


if __name__ == '__main__':
    x = 120
    print(Solution().reverse(x))
