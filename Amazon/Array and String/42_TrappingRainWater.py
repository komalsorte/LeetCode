__author__ = "Komal Atul Sorte"
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def leftMax(self, height, index):
        i = 0
        max = 0
        while i != index + 1:
            if max < height[i]:
                max = height[i]
            i = i + 1
        return max

    def rightMax(self, height, i):
        max = 0
        while i != len(height):
            if max < height[i]:
                max = height[i]
            i = i + 1
        return max

    def trap(self, height):
        if len(height) == 0:
            return 0
        index = 1
        volume = 0
        while index != len(height):
            left_max = self.leftMax(height, index)
            right_max = self.rightMax(height, index + 1)
            minLimit = min(left_max, right_max) - height[index]
            if minLimit > 0:
                volume += minLimit
            index += 1
        return volume


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
