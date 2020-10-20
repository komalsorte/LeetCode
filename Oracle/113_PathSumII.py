"""
LeetCode - Medium
"""
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.paths = list()
    def pathSum(self, root: TreeNode, sum: int):
        if root is None:
            return list()
        paths = []
        self.pathSumHelper(root, sum, 0, [], paths)
        return paths

    def pathSumHelper(self, root, target, count, pathTracker, paths):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if count + root.val == target:
                pathTracker.append(root.val)
                paths.append(list(pathTracker))
                pathTracker.pop()
                return True
            else:
                return False
        pathTracker.append(root.val)
        self.pathSumHelper(root.left, target, count + root.val, pathTracker, paths)
        self.pathSumHelper(root.right, target, count + root.val, pathTracker, paths)
        pathTracker.pop()



if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
    root.right = right
    root.left = left
    # print(Solution().hasPathSum(TreeNode(1, TreeNode(2)), 1))
    print(Solution().pathSum(root, 22))
