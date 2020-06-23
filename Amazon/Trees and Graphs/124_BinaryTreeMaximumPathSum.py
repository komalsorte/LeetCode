__author__ = "Komal Atul Sorte"
"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # maxSum = 0
    #     if root.left is None and root.right is None:
    #         return root.val
    #     else:
    #         maxSum = self.helper(root, float('-inf'))
    #         return maxSum
    #
    # def helper(self, root, maxSum):
    #     if root is None:
    #         return 0
    #     else:
    #         leftSum = max(self.helper(root.left, maxSum), maxSum)
    #         rightSum = max(self.helper(root.right, maxSum), maxSum)
    #         maxSum = max(maxSum, root.val + leftSum + rightSum, root.val + leftSum, root.val + rightSum)
    #     return maxSum
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum

if __name__ == '__main__':
    root = TreeNode(-10)

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # root = TreeNode(1)
    #
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.left.left.left = TreeNode(5)
    # root.left.left.right = TreeNode(6)
    # root.left.right.left = TreeNode(7)
    # root.left.right.right = TreeNode(8)
    #
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)
    # root.right.left.left = TreeNode(8)
    # root.right.left.right = TreeNode(7)
    # root.right.right.left = TreeNode(6)
    # root.right.right.right = TreeNode(5)
    # root = TreeNode(1)
    #
    # root.left = TreeNode(2)
    #
    # root.right = TreeNode(3)
    # root = TreeNode(-3)
    # root = TreeNode(-2)
    # root.left = TreeNode(-1)
    print(Solution().maxPathSum(root=root))
