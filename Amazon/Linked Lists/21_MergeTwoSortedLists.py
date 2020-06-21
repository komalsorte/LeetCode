__author__ = "Komal Atul Sorte"
"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, ll1, ll2):
        if ll1 is None and ll2 is not None:
            return ll2
        elif ll1 is not None and ll2 is None:
            return ll1
        l1, l2, l3 = ll1, ll2, None
        previous, node = None, None
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if l3 is None:
                l3 = node
            else:
                previous.next = node
            previous = node
        if l1 is not None:
            previous.next = l1
        elif l2 is not None:
            previous.next = l2
        return l3

if __name__ == '__main__':
    ll1 = ListNode(1)
    # ll1.next = ListNode(2, ListNode(4))

    ll2 =ListNode(1)
    ll2.next = ListNode(3, ListNode(4))
    print(Solution().mergeTwoLists(ll1, ll2))