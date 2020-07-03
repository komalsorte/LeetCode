__author__ = "Komal Atul Sorte"
"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    output = []

    def postorderTraversalRecurse(self, root):
        self.output = []
        return self.postorderTraversalRecurseHelper(root)

    def postorderTraversalRecurseHelper(self, root):
        if root:
            self.postorderTraversalRecurseHelper(root.left)
            self.postorderTraversalRecurseHelper(root.right)
            self.output.append(root.val)
        return self.output

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        return output[::-1]


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6))
    root.right = right
    root.left = left

    print(Solution().postorderTraversalRecurse(root))
    # root = None
    # print(Solution().preorderTraversalRecurse(root))
    # print(Solution().preorderTraversal(root))
