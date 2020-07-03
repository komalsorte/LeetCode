__author__ = "Komal Atul Sorte"
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def maxDepth(self, root):
        depth = 0
        if root is None:
            return depth

        self.helper(root, depth + 1)

        return self.max_depth - 1

    def helper(self, root, depth):
        depth_left, depth_right = 0, 0
        if root is None:
            self.max_depth = max(depth, self.max_depth)
            return self.max_depth

        depth_left = self.helper(root.left, depth + 1)

        depth_right = self.helper(root.right, depth + 1)

        return max(depth_left, depth_right)


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6))
    root.right = right
    root.left = left

    print(Solution().maxDepth(root))
