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
    def reverseKGroup(self, ll, k):
        current, previous, next, head, index = ll, None, None, ll, 0
        if current is None:
            return None
        while current is not None and index < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            index += 1
        if next is not None:
            head.next = self.reverseKGroup(current, k)
        self.print(previous)
        return previous

    def print(self, previous):
        """

        :return:
        """
        node = previous
        nodes_res = list()
        while node is not None:
            nodes_res.append(str(node.val))
            node = node.next
        print(" -> ".join(nodes_res))


if __name__ == '__main__':
    ll2 = ListNode(1)
    ll2.next = ListNode(3, ListNode(4, ListNode(5)))
    Solution().print(ll2)
    print(Solution().reverseKGroup(ll2, 2))
