__author__ = "Komal Atul Sorte"
"""

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = 0

    def countUnivalSubtrees(self, root):
        if root is None:
            return 1
        self.countUnivalSubtreesHelper(root)
        return self.count

    def countUnivalSubtreesHelper(self, root):
        if root.left is None and root.right is None:
            self.count += 1
            print(root.val)
            return {root.val}

        if root.left is None:
            uniListLeft = set()
        else:
            uniListLeft = self.countUnivalSubtreesHelper(root.left)
        if root.right is None:
            uniListRight = set()
        else:
            uniListRight = self.countUnivalSubtreesHelper(root.right)
        uniListLeft.update(uniListRight)
        if len(uniListLeft) == 1:
            if {root.val} == uniListLeft:
                self.count += 1

        uniListLeft.add(root.val)
        return uniListLeft


if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(1, TreeNode(5), TreeNode(5))
    right = TreeNode(5, None, TreeNode(5))
    root.right = right
    root.left = left

    print(Solution().countUnivalSubtrees(root))
