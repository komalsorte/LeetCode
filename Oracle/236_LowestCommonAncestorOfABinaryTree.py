"""
LeetCode - Medium
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        pPath, qPath = [], []
        self.findNodePath(root, p, pPath)
        self.findNodePath(root, q, qPath)

        pindex = 0
        qindex = 0

        while True:
            if pPath[pindex] == qPath[qindex]:
                break
            else:
                qindex += 1
            if qindex == len(qPath):
                qindex = 0
                pindex += 1
        return pPath[pindex]

    def findNodePath(self, root, node, path):
        if root is None:
            return False
        if root.val == node.val:
            path.append(root)
            return True
        left = self.findNodePath(root.left, node, path)
        right = self.findNodePath(root.right, node, path)
        if left or right:
            path.append(root)
            return True
        return False


if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    right = TreeNode(1, TreeNode(0), TreeNode(8))
    root.left = left
    root.right = right

    ans = Solution().lowestCommonAncestor(root, TreeNode(7), TreeNode(4))
