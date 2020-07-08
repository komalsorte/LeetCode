__author__ = "Komal Atul Sorte"

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


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
        serialize_res = ''
        serialize_res = self.serializeHelper(root, serialize_res)
        return serialize_res

    def serializeHelper(self, root, serialize_res):
        if root is None:
            serialize_res = serialize_res + 'None,'
        else:
            serialize_res = serialize_res + str(root.val) + ','
            serialize_res = self.serializeHelper(root.left, serialize_res)
            serialize_res = self.serializeHelper(root.right, serialize_res)
        return serialize_res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        tree = self.deserializeHelper(data)
        return tree

    def deserializeHelper(self, data):
        if data[0] == 'None':
            data.pop(0)
            return None
        else:
            root = TreeNode(data[0])
            data.pop(0)
            root.left = self.deserializeHelper(data)
            root.right = self.deserializeHelper(data)
            return root




# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3, TreeNode(4), TreeNode(5))
root.left = left
root.right = right
codec.deserialize(codec.serialize(root))
