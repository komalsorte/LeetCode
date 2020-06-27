__author__ = "Komal Atul Sorte"
"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""


class Solution:

    def guessNumber(self, n):
        left, right = 0, n
        mid = int((left + right) / 2)

        while left <= right:
            score = guess(mid)
            if score == 0:
                return mid
            if score == -1:
                right = mid - 1
            elif score == 1:
                left = mid + 1
            mid = int((left + right) / 2)
        return -1


if __name__ == '__main__':
    num = 10
    print(Solution().guessNumber(n=num))
