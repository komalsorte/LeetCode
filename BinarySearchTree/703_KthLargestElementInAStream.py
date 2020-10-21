"""
LeetCode - Easy
"""

"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class KthLargest:
    # Exceeds time limit
    def __init__(self, k: int, nums):
        self.nums = nums
        self.k = k
        self.tree = None
        self.createBST(nums)
        self.klarge = []
        self.kcount = 0

    def add(self, val: int):
        self.tree = self.insert(val, self.tree)
        self.klarge = []
        self.kcount = 0
        self.search(self.tree)
        return self.klarge[self.k - 1]

    def createBST(self, nums):
        for n in nums:
            self.tree = self.insert(n, self.tree)

    def insert(self, num, root):
        if root is None:
            return TreeNode(num)
        else:
            if num < root.val:
                root.left = self.insert(num, root.left)
            else:
                root.right = self.insert(num, root.right)
            return root

    def search(self, root):
        if root is None:
            return

        if self.kcount == self.k:
            return

        self.search(root.right)
        if self.kcount != self.k:
            self.kcount += 1
            self.klarge.append(root.val)

        self.search(root.left)


if __name__ == '__main__':
    k = 3
    nums = [4, 5, 8, 2]
    obj = KthLargest(k, nums)
    print(obj.add(9))
    print(obj.add(10))
    print(obj.add(11))
