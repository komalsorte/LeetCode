"""
LeetCode - Easy
"""
"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diff = float("inf")
        self.ele = None

    def closestValue(self, root: TreeNode, target: float) -> int:
        if root is not None:
            self.closestValue(root.left, target)
            if abs(target - root.val) < self.diff:
                self.diff = abs(target - root.val)
                self.ele = root.val
            elif abs(target - root.val) > self.diff:
                return self.ele
            self.closestValue(root.right, target)
        return self.ele


if __name__ == '__main__':
    root = TreeNode(6)
    left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    right = TreeNode(8, TreeNode(7), TreeNode(9))
    root.left = left
    root.right = right
    print(Solution().closestValue(root, 3.5))
