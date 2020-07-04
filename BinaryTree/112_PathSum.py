__author__ = "Komal Atul Sorte"
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    isPath = False
    root_val = None

    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        else:
            self.root_val = root.val
            self.hasSumHelper(root, sum, 0)
            return self.isPath

    def hasSumHelper(self, root, sum, total):
        if root is not None:
            total = total + root.val
            print(total)
            self.hasSumHelper(root.left, sum, total)
            self.hasSumHelper(root.right, sum, total)
        else:
            if sum == total and sum != self.root_val:
                self.isPath = True


if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(4)
    left.left = TreeNode(11, TreeNode(7), TreeNode(2))
    root.left = left

    right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

    root = TreeNode(1, TreeNode(2))
    print(Solution().hasPathSum(root, 1))
