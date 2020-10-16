"""
LeetCode - Easy
"""
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        if current == None or current.next == None:
            return head
        else:
            next = head.next
        while next != None:
            if current.val == next.val:
                current.next = next.next
                next.next = None
                next = current.next
            else:
                current = next
                next = current.next
        return head


if __name__ == '__main__':
    ll2 = ListNode(1)
    ll2.next = ListNode(1, ListNode(2, ListNode(2, ListNode(3))))
    print(Solution().deleteDuplicates(ll2))
