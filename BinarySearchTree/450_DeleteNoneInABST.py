__author__ = "Komal Atul Sorte"
"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.isPValue = False

    def successor(self, root: 'TreeNode') -> 'TreeNode':
        root = root.right
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        450 - Delete Node in a BST
        :param root:
        :param key:
        :return:
        """
        if root is None:
            return
        if root.val == key:
            # if 0 child
            # direct delete
            if root.left is None and root.right is None:
                root = None

            # if 2 children
            # find in-order successor and replace the node
            elif root.left and root.right:
                inorderSuccessor = self.successor(root)
                root = self.deleteNode(root, inorderSuccessor.val)
                inorderSuccessor.left = root.left
                inorderSuccessor.right = root.right
                root = inorderSuccessor

            # if 1 child
            # replace root by child
            elif root.left or root.right:
                if root.left:
                    root = root.left
                else:
                    root = root.right

            return root

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            root.right = self.deleteNode(root.right, key)
            return root


if __name__ == '__main__':
    root = TreeNode(4)
    left = TreeNode(2, TreeNode(1), TreeNode(3))
    right = TreeNode(10, TreeNode(9, TreeNode(8, TreeNode(5, None, TreeNode(6)))))
    root.right = right
    root.left = left

    # root = TreeNode(1, TreeNode(1))
    val = 5
    ans = Solution().deleteNode(root, 10)
    print(ans)
