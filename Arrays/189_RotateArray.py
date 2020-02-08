"""
Easy
"""

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        temp.extend(nums)
        for i in range(k):
            last = temp[len(temp) - 1]
            temp = temp[:len(temp) - 1]
            temp = [last] + temp
        nums.clear()
        nums.extend(temp)
        return nums

if __name__ == '__main__':
    print(Solution().rotate([-1,-100,3,99], 2))