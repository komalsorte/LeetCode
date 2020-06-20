__author__ = 'Komal Atul Sorte'
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""


class Solution:
    # time complexity - n2 - brute force approch
    # exceeds time limit
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * abs(i - j)
                max_area = max(max_area, area)
        return max_area

    # Time comp - O(n) - didnt understand the logic - +/-
    def maxArea_n(self, height):
        max_area, l, r = 0, 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * abs(l - r)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea_n(height))
