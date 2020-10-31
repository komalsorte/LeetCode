class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children
class Solution:
    def __init__(self):
        self.visitedSet = set()
    def isValidGraph(self, node):

        self.visitedSet.add(node)

        for child in node.children:
            self.isValidGraphHelper(child, node)
        return True

    def isValidGraphHelper(self, child, node):
        if node in self.visitedSet:
            return False
        else:
            self.visitedSet.add(node)

        for child in node.children:
            self.isValidGraphHelper(child, node)
        return True


if __name__ == '__main__':

    print(Solution().isValidGraph(node))