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
    flag = False

    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        self.flag = False
        return self.insertIntoBSTHelper(root, val)

    def insertIntoBSTHelper(self, root, val):
        if val < root.val:
            if root.left is None and self.flag == False:
                root.left = TreeNode(val)
                self.flag = True
                return root
            else:
                self.insertIntoBSTHelper(root.left, val)
        elif val > root.val:
            if root.right is None and self.flag == False:
                root.right = TreeNode(val)
                return root
            else:
                self.insertIntoBSTHelper(root.right, val)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    left = TreeNode(2, TreeNode(1), TreeNode(3))
    right = TreeNode(7, None, TreeNode(8))
    root.right = right
    root.left = left

    # root = TreeNode(1, TreeNode(1))
    val = 5
    ans = Solution().insertIntoBST(root, val)
    print(ans)
