"""
LeetCode - Medium
"""
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:

            # Find center
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.val)

            # reverse it
            current = slow.next
            slow.next = None
            previous = None
            next_node = None
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            ll2, ll1 = previous, head
            current, previous, next_node = None, None, None

            # merge
            while ll2:
                ll1_next = ll1.next
                ll2_next = ll2.next

                ll2.next = ll1_next
                ll1.next = ll2

                ll2 = ll2_next
                ll1 = ll1_next

if __name__ == '__main__':
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    print(Solution().reorderList(root))
