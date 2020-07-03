__author__ = "Komal Atul Sorte"
"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    output = []

    def preorderTraversalRecurse(self, root):
        self.output = []
        return self.preorderTraversalRecurseHelper(root)

    def preorderTraversalRecurseHelper(self, root):
        if root:
            self.output.append(root.val)
            self.preorderTraversalRecurseHelper(root.left)
            self.preorderTraversalRecurseHelper(root.right)
        return self.output

    # Root - Left - Right
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        stack, output = [root], []

        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6))
    root.right = right
    root.left = left

    print(Solution().preorderTraversalRecurse(root))
    root = None
    print(Solution().preorderTraversalRecurse(root))
    print(Solution().preorderTraversal(root))
