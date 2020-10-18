class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.preorder = list()
        self.inorder = list()
        self.postorder = list()
        self.levelorder = list()

    def preorderTraversal(self, root):
        self.preorderTraversalRecurse(root)
        return self.preorder

    def preorderTraversalRecurse(self, root):
        if root is None:
            return
        self.preorder.append(root.val)
        self.preorderTraversalRecurse(root.left)
        self.preorderTraversalRecurse(root.right)

    def inorderTraversal(self, root):
        self.inorderTraversalRecurse(root)
        return self.inorder

    def inorderTraversalRecurse(self, root):
        if root is None:
            return

        self.inorderTraversalRecurse(root.left)
        self.inorder.append(root.val)
        self.inorderTraversalRecurse(root.right)

    def postorderTraversal(self, root):
        self.postorderTraversalRecurse(root)
        return self.postorder

    def postorderTraversalRecurse(self, root):
        if root is None:
            return
        self.postorderTraversalRecurse(root.left)
        self.postorderTraversalRecurse(root.right)
        self.postorder.append(root.val)

    def levelorderTraversal(self, root):
        self.levelorderTraversalRecurse(root, 0)
        return self.levelorder

    def levelorderTraversalRecurse(self, root, level):
        if root is None:
            return
        if len(self.levelorder) == level:
            self.levelorder.append([])
        self.levelorder[level] = self.levelorder[level] + [root.val]

        self.levelorderTraversalRecurse(root.left, level + 1)
        self.levelorderTraversalRecurse(root.right, level + 1)


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6))
    root.right = right
    root.left = left

    print(Solution().preorderTraversalRecurse(root))
    # root = None
    print(Solution().levelorderTraversal(root))
    # print(Solution().preorderTraversal(root))
