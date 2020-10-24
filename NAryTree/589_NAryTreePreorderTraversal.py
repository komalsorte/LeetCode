"""
LeetCode - Easy
"""
"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output

    def preorderRecurse(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        preorder = list()
        self.preorderRecurseHelper(root, preorder)
        return preorder

    def preorderRecurseHelper(self, root, preorder):
        if root is None:
            return
        preorder.append(root.val)
        for child in root.children:
            self.preorderRecurseHelper(child, preorder)



if __name__ == '__main__':
    NodeA = Node(3)
    NodeB = Node(2)
    NodeC = Node(4, [Node(5), Node(6)])
    root = Node(1, [NodeA, NodeB, NodeC])
    print(Solution().preorder(root))
