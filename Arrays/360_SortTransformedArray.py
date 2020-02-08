"""
Medium - Incomplete
"""
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        x = ''
        equation = (a * x * x) + (b * x) + c

        for index in range(len(nums)):
            pass



if __name__ == '__main__':
    print(Solution().sortTransformedArray([-4, -2, 2, 4], a=1, b=3, c=5))
