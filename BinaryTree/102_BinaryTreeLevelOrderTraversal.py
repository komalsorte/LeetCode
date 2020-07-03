__author__ = "Komal Atul Sorte"

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        levels = self.helper(root, 0, levels)
        return levels

    def helper(self, root, level, levels):
        if len(levels) == level:
            levels.append([])

        levels[level].append(root.val)

        if root.left:
            levels = self.helper(root.left, level + 1, levels)
        if root.right:
            levels = self.helper(root.right, level + 1, levels)
        return levels

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6))
    root.right = right
    root.left = left

    print(Solution().levelOrder(root))
