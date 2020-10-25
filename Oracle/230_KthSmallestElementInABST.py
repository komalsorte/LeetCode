"""
LeetCode - Medium
"""
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if k <= 0:
            return None
        result = self.kthSmallestHelper(root, k, list())
        return result[-1]

    def kthSmallestHelper(self, root, k, result):
        if root is None:
            return

        self.kthSmallestHelper(root.left, k, result)
        if len(result) < k:
            result.append(root.val)
        if len(result) >= k:
            return result
        self.kthSmallestHelper(root.right, k, result)

        return result


if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(8, TreeNode(6), TreeNode(10))
    root.right = right
    root.left = left

    print(Solution().kthSmallest(root, 0))
