"""


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.isPValue = False

    def isValidBST(self, root):
        """
        98. Validate Binary Search Tree
        :param root:
        :return:
        """
        result = self.isValidBSTHelper(root, float('-inf'), float('inf'))
        return result

    def isValidBSTHelper(self, root, lower, upper):
        if root is None:
            return True
        if root.val > lower and root.val < upper:
            isLeftBST = self.isValidBSTHelper(root.left, lower, root.val)
            isRightBST = self.isValidBSTHelper(root.right, root.val, upper)
            return isLeftBST and isRightBST
        else:
            return False

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """
        285. Inorder Successor in BST

        :param root:
        :param p:
        :return:
        """
        if root is None:
            return None

        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        if self.isPValue:
            self.isPValue = False
            return root
        if root.val == p.val and self.isPValue is False:
            self.isPValue = True

        right = self.inorderSuccessor(root.right, p)
        if right:
            return right
        return None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        700 - Search in a Binary Search Tree
        :param root:
        :param val:
        :return:
        """
        if root == None or root.val == val:
            return root
        elif val < root.val:
            subtree = self.searchBST(root.left, val)
            return subtree
        else:
            subtree = self.searchBST(root.right, val)
            return subtree

    def insertIntoBST(self, root, val):
        """
        701 - Insert into a Binary Search Tree
        :param root:
        :param val:
        :return:
        """
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def successor(self, root: 'TreeNode') -> 'TreeNode':
        """
        285. Inorder Successor in BST

        :param root:
        :param p:
        :return:
        """
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
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(Solution().isValidBST(root))


    root = TreeNode(4)
    left = TreeNode(2, TreeNode(-1, TreeNode(-2), TreeNode(1, TreeNode(0))), TreeNode(3))
    right = TreeNode(7)
    root.left = left
    root.right = right
    ans = Solution().inorderSuccessor(root, TreeNode(4))
    print(ans.val)

    val = -2
    ans = Solution().searchBST(root, val)
    if ans is None:
        print(None)
    else:
        print(ans.val)


    ans = Solution().insertIntoBST(root, -3)

    ans = Solution().deleteNode(root, -1)
    print(ans)