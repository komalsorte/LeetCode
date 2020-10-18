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
        self.maxDepth = 0
        self.uniValueSubtreesCounter = 0

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

    def maximumDepthOfBinaryTree(self, root):
        """
        104_MaximumDepthOfBinaryTree
        :return:
        """
        if root is not None:
            self.maximumDepthOfBinaryTreeHelper(root, 1)
        return self.maxDepth

    def maximumDepthOfBinaryTreeHelper(self, root, level):
        if root is None:
            return
        if level >= self.maxDepth:
            self.maxDepth = level
        self.maximumDepthOfBinaryTreeHelper(root.left, level + 1)
        self.maximumDepthOfBinaryTreeHelper(root.right, level + 1)

    def maximumDepthOfBinaryTreeApproachTwo(self, root):
        """
        104_MaximumDepthOfBinaryTree
        :return:
        """
        if root is None:
            return 0
        left_max = self.maximumDepthOfBinaryTreeApproachTwo(root.left)
        right_max = self.maximumDepthOfBinaryTreeApproachTwo(root.right)
        return max(left_max, right_max) + 1

    def hasPathSum(self, root, sum):
        """
        112 - Path Sum
        :return:
        """
        if root is None:
            return False
        return self.hasPathSumHelper(root, sum, 0)

    def hasPathSumHelper(self, root, sum, count):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if sum == (count + root.val):
                return True
            else:
                return False


        hasPathLeftSubtree = self.hasPathSumHelper(root.left, sum, count + root.val)
        hasPathRightSubtree = self.hasPathSumHelper(root.right, sum, count + root.val)
        return hasPathLeftSubtree or hasPathRightSubtree

    def countUnivalSubtrees(self, root):
        """
        250 - Count Univalue Subtrees
        :param root:
        :return:
        """
        self.countUnivalSubtreesHelper(root)
        return self.uniValueSubtreesCounter

    def countUnivalSubtreesHelper(self, root):
        if root is None:
            return set()

        if root.left is None and root.right is None:
            self.uniValueSubtreesCounter += 1
            return {root.val}


        leftSet = self.countUnivalSubtreesHelper(root.left)
        rightSet = self.countUnivalSubtreesHelper(root.right)
        leftSet.update(rightSet)
        leftSet.add(root.val)
        if len(leftSet) == 1:
            self.uniValueSubtreesCounter += 1
        return leftSet

    def isSymmetric(self, root):
        """
        101 - Symmetric Tree
        :param root:
        :return:
        """
        return self.isSymmetricHelper(root, root)

    def isSymmetricHelper(self, subtree_1, subtree_2):
        if subtree_1 is None and subtree_2 is None:
            return True
        elif subtree_1 is not None and subtree_2 is not None:
            if subtree_1.val == subtree_2.val:
                flag_1 = self.isSymmetricHelper(subtree_1.left, subtree_2.right)
                flag_2 = self.isSymmetricHelper(subtree_1.right, subtree_2.left)
                return flag_1 and flag_2

            else:
                return False
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(7, TreeNode(5), TreeNode(6, TreeNode(8, TreeNode(9))))
    root.right = right
    root.left = left

    print(Solution().preorderTraversalRecurse(root))
    # root = None
    print(Solution().levelorderTraversal(root))
    print(Solution().maximumDepthOfBinaryTreeApproachTwo(root))

    root = TreeNode(5)
    left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    root.right = right
    root.left = left
    # print(Solution().hasPathSum(TreeNode(1, TreeNode(2)), 1))
    print(Solution().hasPathSum(TreeNode(1, TreeNode(2)), 1))

    root = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
    print(Solution().countUnivalSubtrees(root))

    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, None, TreeNode(3)))
    print(Solution().isSymmetric(root))
