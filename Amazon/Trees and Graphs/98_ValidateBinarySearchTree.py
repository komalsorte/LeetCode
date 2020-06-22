__author__ = "Komal Atul Sorte"
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
"""


# inf - unbounded upper value for comparison

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    """
    :type root: TreeNode
    :rtype: bool
    """

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        # def helper(node, lower=float('-inf'), upper=float('inf')):
        #     if not node:
        #         return True
        #
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False
        #
        #     if not helper(node.right, val, upper):
        #         return False
        #     if not helper(node.left, lower, val):
        #         return False
        #     return True
        #
        # return helper(root)


if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(8, TreeNode(6), TreeNode(10))
    root.right = right
    root.left = left

    print(Solution().isValidBST(root))
