__author__ = "Komal Atul Sorte"
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        class Wrapper():
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next


if __name__ == '__main__':
    ll1 = ListNode(1)
    ll1.next = ListNode(2, ListNode(4))

    ll2 = ListNode(1)
    ll2.next = ListNode(3, ListNode(4))
    ll3 = ListNode(1)
    ll2.next = ListNode(5, ListNode(8))
    lists = [ll1, ll2, ll3]
    print(Solution().mergeKLists(lists))
