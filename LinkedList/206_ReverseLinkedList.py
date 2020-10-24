"""
LeetCode - Easy
"""
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        previous = None
        node = head
        node_next = head.next
        while node is not None:
            node_next = node.next
            node.next = previous
            previous = node
            node = node_next
        return previous



if __name__ == '__main__':
    intersection = ListNode(3, ListNode(4, ListNode(5)))
    node = ListNode(1, ListNode(2, intersection))
    print(
        Solution().reverseList(node)
    )
