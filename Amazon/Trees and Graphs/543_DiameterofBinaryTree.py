__author_ = "Komal Atul Sorte"
"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        self.dfs(root)
        return self.max_diameter - 1

    def dfs(self, root):
        if root is None:
            return 0

        left_subtree = max(self.dfs(root.left), 0)
        right_subtree = max(self.dfs(root.right), 0)

        self.max_diameter = max(left_subtree, right_subtree, 1 + left_subtree + right_subtree)
        return 1 + max(left_subtree, right_subtree)
if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2, TreeNode(4), TreeNode(5))
    right = TreeNode(3)
    root.right = right
    root.left = left

    root_6 = TreeNode(6, TreeNode(0, None, TreeNode(-1)), TreeNode(5, TreeNode(-4), None))
    root_9 = TreeNode(9, root_6)
    root_minus7 = TreeNode(-7, TreeNode(-6, TreeNode(5)), TreeNode(-6, TreeNode(9, TreeNode(-2))))
    root_minus9 = TreeNode(-9, root_9, root_minus7)
    root_minus3 = TreeNode(-3, root_minus9, TreeNode(-3, TreeNode(-4)))
    root = TreeNode(4, TreeNode(-7), root_minus3)
    print(Solution().diameterOfBinaryTree(root))

    # Failed: 102 / 106 test cases passed.
    # [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
