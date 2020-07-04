__author__ = "Komal Atul Sorte"
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
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

    def isMirror(self, subtree1, subtree2):
        if subtree1 is None and subtree2 is None:
            return True
        elif subtree1 is not None and subtree2 is not None:
            if subtree1.val == subtree2.val:
                flag1 = self.isMirror(subtree1.left, subtree2.right)
                flag2 = self.isMirror(subtree1.right, subtree2.left)

                return flag1 and flag2
            else:
                return False
        else:
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
