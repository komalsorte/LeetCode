__author__ = "Komal Atul Sorte"
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode):
        return self.isMirror(root, root)

    def isMirror(self, subroot_1, subroot_2):
        if subroot_1 is None and subroot_2 is None:
            return True
        if subroot_1 is not None and subroot_2 is not None:
            if subroot_1.val == subroot_2.val:
                print(subroot_1.val, subroot_1.val)
                return self.isMirror(subroot_1.left, subroot_2.right) and self.isMirror(subroot_1.right, subroot_2.left)
        return False

if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.right = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left.left = TreeNode(8)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(5)

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(2)

    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(Solution().isSymmetric(root=root))

