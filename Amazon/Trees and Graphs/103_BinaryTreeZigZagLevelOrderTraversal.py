__author__ = "Komal Atul Sorte"
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
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

        if level % 2 == 1:
            levels[level].insert(0, root.val)
        else:
            levels[level].append(root.val)

        if root.left:
            levels = self.helper(root.left, level + 1, levels)
        if root.right:
            levels = self.helper(root.right, level + 1, levels)
        return levels


if __name__ == '__main__':
    root = TreeNode(3)

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # root = TreeNode(1)
    #
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.left.left.left = TreeNode(5)
    # root.left.left.right = TreeNode(6)
    # root.left.right.left = TreeNode(7)
    # root.left.right.right = TreeNode(8)
    #
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)
    # root.right.left.left = TreeNode(8)
    # root.right.left.right = TreeNode(7)
    # root.right.right.left = TreeNode(6)
    # root.right.right.right = TreeNode(5)
    print(Solution().zigzagLevelOrder(root=root))
