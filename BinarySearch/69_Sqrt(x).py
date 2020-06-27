__author__ = "Komal Atul Sorte"
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x):
        if x == 1:
            return 1
        left, right = 0, int(x / 2)
        mid = int((left + right) / 2)

        while left <= right:
            sqr = mid * mid
            if sqr == x:
                return int(mid)
            elif sqr < x:
                left = mid + 1
            else:
                right = mid - 1
            mid = int((left + right) / 2)
        return right


if __name__ == '__main__':
    num = 9
    print(Solution().mySqrt(x=num))
