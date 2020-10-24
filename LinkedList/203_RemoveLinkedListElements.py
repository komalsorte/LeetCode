"""
LeetCode - Easy
"""
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        previous = None
        while node is not None:
            if node.val == val:
                if previous is not None:
                    previous.next = node.next
                    node.next = None
                    node = previous.next
                else:
                    head = head.next
                    node.next = None
                    node = head
            else:
                previous = node
                node = node.next
        return head


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(1, ListNode(3, ListNode(4, ListNode(1))))))
    print(Solution().removeElements(node, 1))
