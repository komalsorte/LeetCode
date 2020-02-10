"""
Easy
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        coins = 0
        while coins < n:
            if (n - coins) >= (count + 1):
                coins = coins + count + 1
                count = count + 1
            else:
                break
        return count


if __name__ == '__main__':
    print(Solution().arrangeCoins(5))
