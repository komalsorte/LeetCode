__author__ = "Komal Atul Sorte"
"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, ll):
        current, previous, next = ll, None, None
        if current is None:
            return None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous


if __name__ == '__main__':
    ll2 = ListNode(1)
    ll2.next = ListNode(3, ListNode(4))
    print(Solution().reverse(ll2))
