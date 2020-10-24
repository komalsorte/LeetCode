"""
LeetCode - Medium
"""
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        tracker = dict()
        node, index = head, 1
        while node is not None:
            tracker[index] = node
            node = node.next
            index += 1

        index = len(tracker) - n + 1
        if index == 1:
            head = tracker[index].next
        else:
            tracker[index - 1].next = tracker[index].next

        tracker[index] = None
        return head


if __name__ == '__main__':
    intersection = ListNode(3, ListNode(4, ListNode(5)))
    node1 = ListNode(1, ListNode(2, intersection))
    print(Solution().removeNthFromEnd(node1, 2))
