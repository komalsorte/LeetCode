__author__ = "Komal Atul Sorte"
"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    tree= None
    def insertIntoBST(self, root, val):
        self.tree = root
        self.insertIntoBSTHelper(root, val)

    def insertIntoBSTHelper(self, root, val):
        if val < root.val:
            self.insertIntoBSTHelper(root.left, val)
        elif val > root.val:
            self.insertIntoBSTHelper(root.right, val)
