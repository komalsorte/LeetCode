__author__ = "Komal Atul Sorte"
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    root = None
    def __init__(self, root: TreeNode):
        self.root = root
        self.last_smallest_index = 0
        self.nodes = []
        self._inorder(self.root)
        print(self.nodes)


    def _inorder(self, root: TreeNode):
        if root is None:
            return root
        self._inorder(root.left)
        self.nodes.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.last_smallest_index < len(self.nodes):
            self.last_smallest_index += 1
        return self.nodes[self.last_smallest_index - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        pass
        if self.last_smallest_index < len(self.nodes):
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(5)
left = TreeNode(3, TreeNode(2), TreeNode(4))
right = TreeNode(8, TreeNode(6), TreeNode(10))
root.right = right
root.left = left
obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
