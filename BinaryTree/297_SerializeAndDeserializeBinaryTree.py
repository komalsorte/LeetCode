"""
LeetCode - Hard
"""
"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = self.serializeHelper(root, "")
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(","))
        nodes.pop()
        tree = None
        tree = self.deserializeHelper(nodes)
        return tree

    def deserializeHelper(self, nodes):
        if len(nodes) == 0:
            return
        if nodes[0] == "None":
            nodes.popleft()
            return None

        root = TreeNode(int(nodes[0]))
        nodes.popleft()
        root.left = self.deserializeHelper(nodes)
        root.right = self.deserializeHelper(nodes)

        return root


    def serializeHelper(self, root, result):
        if root is None:
            result += str("None") + ","
            return result
        result += str(root.val) + ","
        result = self.serializeHelper(root.left, result)
        result = self.serializeHelper(root.right, result)
        return result


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3, TreeNode(4), TreeNode(5))
    root.right = right
    root.left = left
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
