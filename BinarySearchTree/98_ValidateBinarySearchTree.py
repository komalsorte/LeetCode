__author__ = "Komal Atul Sorte"
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    previous = None
    flag = True
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        if self.previous == None:
            self.previous = root.val
        else:
            if root.val <= self.previous:
                self.flag = False
            self.previous = root.val

        self.inorderTraversal(root.right)

    def isValidBST(self, root):
        self.inorderTraversal(root)
        return self.flag

if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(9, TreeNode(2), TreeNode(4))
    right = TreeNode(8, TreeNode(6), TreeNode(10))
    root.right = right
    root.left = left

    root = TreeNode(1, TreeNode(1))

    print(Solution().isValidBST(root))
