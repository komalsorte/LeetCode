__author__ = "Komal Atul Sorte"
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    output = []

    def inorderTraversalRecurse(self, root):
        self.output = []
        return self.inorderTraversalRecurseHelper(root)

    def inorderTraversalRecurseHelper(self, root):
        if root:
            self.inorderTraversalRecurseHelper(root.left)
            self.output.append(root.val)
            self.inorderTraversalRecurseHelper(root.right)
        return self.output

    def inorderTraversal(self, root):
        if root is None:
            return None
        stack, output = [], []

        while True:
            while root is not None:
                print(root.val)
                stack.append(root)
                root = root.left
            if len(stack) != 0:
                root = stack.pop()
                output.append(root.val)
                root = root.right
            else:
                break

        return output


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6))
    root.right = right
    root.left = left

    # print(Solution().inorderTraversalRecurse(root))
    # print(Solution().inorderTraversalRecurse(root))
    print(Solution().inorderTraversal(root))
