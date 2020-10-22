"""
LeetCode - Easy
"""
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        path = []

        def rangeSumBSTHelper(root, L, R, path):
            if root is None:
                return
            if root.val >= L and root.val <= R:
                path.append(root.val)

            rangeSumBSTHelper(root.left, L, R, path)
            rangeSumBSTHelper(root.right, L, R, path)

        rangeSumBSTHelper(root, L, R, path)
        print(sum(path))
        return sum(path)
