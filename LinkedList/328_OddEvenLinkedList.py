"""
LeetCode - Medium
"""
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        even_start = head.next
        even_head = head.next
        odd_head = head

        while even_head is not None and even_head.next is not None:
            odd_head.next = even_head.next
            # odd_head = odd_head.next
            if odd_head.next is not None:
                even_head.next = odd_head.next.next
                even_head = even_head.next
                odd_head = odd_head.next
        odd_head.next = even_start
        return head


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().oddEvenList(node))
