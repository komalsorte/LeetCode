"""
LeetCode - Easy
"""
"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution(object):
    def postorderRecurse(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        postorder = list()
        self.postorderRecurseHelper(root, postorder)
        return postorder


    def postorderRecurseHelper(self, root, postorder):
        if root is None:
            return
        for child in root.children:
            self.postorderRecurseHelper(child, postorder)
        postorder.append(root.val)

    def postorder(self, root):
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::])
        output.reverse()
        return output


if __name__ == '__main__':
    NodeA = Node(3, [Node(5), Node(6)])
    NodeB = Node(2)
    NodeC = Node(4, [Node(15), Node(16)])
    root = Node(1, [NodeA, NodeB, NodeC])
    print(Solution().postorder(root))