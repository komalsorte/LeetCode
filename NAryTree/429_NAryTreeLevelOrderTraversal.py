"""
LeetCode - Medium
"""
"""

"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        levelorder = list()
        self.levelOrderHelper(root, levelorder, 0)
        return levelorder

    def levelOrderHelper(self, root, levelorder, level):
        if root is None:
            return
        if len(levelorder) == level:
            levelorder.append([])
        levelorder[level].append(root.val)
        for child in root.children:
            self.levelOrderHelper(child, levelorder, level + 1)


if __name__ == '__main__':
    NodeA = Node(3, [Node(5), Node(6)])
    NodeB = Node(2)
    NodeC = Node(4, [Node(15), Node(16)])
    root = Node(1, [NodeA, NodeB, NodeC])
    print(Solution().levelOrder(root))
