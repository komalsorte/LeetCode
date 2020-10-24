"""
LeetCode - Easy
"""
"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        head_node = head
        l1_itr = l1
        l2_itr = l2
        double = False
        while l1_itr is not None and l2_itr is not None:
            if l1_itr.val == l2_itr.val:
                node = ListNode(l1_itr.val, ListNode(l2_itr.val))
                l1_itr = l1_itr.next
                l2_itr = l2_itr.next
                double = True

            elif l1_itr.val < l2_itr.val:
                node = ListNode(l1_itr.val)
                l1_itr = l1_itr.next

            else:
                node = ListNode(l2_itr.val)
                l2_itr = l2_itr.next


            head_node.next = node
            head_node = head_node.next
            if double:
                head_node = head_node.next
                double = False

        if l2_itr is None:
            head_node.next = l1_itr
        else:
            head_node.next = l2_itr
        return head.next





if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(5, ListNode(6))))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    print(Solution().mergeTwoLists(l1, l2))
