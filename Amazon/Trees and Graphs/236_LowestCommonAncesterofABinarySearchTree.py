__author__ = "Komal Atul Sorte"

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestorHelper(root, p, q)

    def lowestCommonAncestorHelper(self, root, p, q):
        if root is None or root.val == p.val or root.val == q.val:
            return root
        left_subtree = self.lowestCommonAncestorHelper(root.left, p, q)
        right_subtree = self.lowestCommonAncestorHelper(root.right, p, q)

        if right_subtree is None:
            return left_subtree
        elif left_subtree is None:
            return right_subtree
        else:
            return root


if __name__ == '__main__':
    root = TreeNode(3)

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    p = TreeNode(15)
    q = TreeNode(7)
    root.right.left = p
    root.right.right = q

    root = TreeNode(3)

    root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))

    root.right = TreeNode(1, TreeNode(0), TreeNode(8))
    p = TreeNode(1)
    q = TreeNode(8)

    print(Solution().lowestCommonAncestor(root, p, q))
