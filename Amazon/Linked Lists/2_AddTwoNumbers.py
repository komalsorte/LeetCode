__author__ = "Komal Atul Sorte"

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Method 1: based on Data Structure repo
"""


class Node:
    """

    """

    def __init__(self, data=None):
        """

        :param data:
        """
        self.data = data
        self.next = None


class LinkedList:
    """

    """

    def __init__(self):
        """

        """
        self.head = None

    def insertUsingList(self, nodes):
        """

        :param nodes:
        :return:
        """
        previous = None
        for n in nodes:
            node = Node(n)
            if self.head == None:
                self.head = node
            else:
                previous.next = node
            previous = node

    def print(self):
        """

        :return:
        """
        node = self.head
        nodes_res = list()
        while node is not None:
            nodes_res.append(str(node.data))
            node = node.next
        print(" -> ".join(nodes_res))

    def addTwoNumbers(self, ll1, ll2):
        ll3 = LinkedList()
        carry = 0
        previous = None

        l1, l2 = ll1.head, ll2.head
        while l1 is not None or l2 is not None:
            if l1 is None:
                sum = l2.data + carry
                l2 = l2.next
            elif l2 is None:
                sum = l1.data + carry
                l1 = l1.next
            else:
                sum = l1.data + l2.data + carry
                l1, l2 = l1.next, l2.next
            carry = sum / 10
            print(int(sum % 10))
            node = Node(sum % 10)
            if ll3.head is None:
                ll3.head = node
            else:
                previous.next = node
            previous = node
        if int(carry) == 1:
            previous.next = Node(int(carry))
        ll3.print()
        return ll3


"""
Method 2: Based on classes defined by LeetCode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, ll1: ListNode, ll2: ListNode) -> ListNode:
        ll3 = None
        carry = 0
        previous = ll3

        l1, l2 = ll1, ll2
        while l1 is not None or l2 is not None:
            if l1 is None:
                sum = l2.val + carry
                l2 = l2.next
            elif l2 is None:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            carry = sum / 10
            print(int(sum % 10))
            node = ListNode(int(sum % 10))
            if ll3 is None:
                ll3 = node
            else:
                previous.next = node
            previous = node
        if int(carry) > 0:
            previous.next = ListNode(int(carry))

        return ll3


if __name__ == '__main__':
    linkedList = LinkedList()

    ll1, ll2 = LinkedList(), LinkedList()
    # ll1.insertUsingList([2, 4, 3])
    # ll2.insertUsingList([5, 6, 4])
    # ll2.print()
    # ll1.insertUsingList([2, 4])
    # ll2.insertUsingList([5, 6, 4])
    # ll1.insertUsingList([])
    # ll2.insertUsingList([5, 6, 4])
    ll1.insertUsingList([5])
    ll2.insertUsingList([5])
    print(linkedList.addTwoNumbers(ll1, ll2))
