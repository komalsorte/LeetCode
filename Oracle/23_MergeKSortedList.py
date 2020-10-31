"""
LeetCode - Hard
"""
from queue import PriorityQueue
import heapq
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        # q = PriorityQueue()
        # for l in lists:
        #     if l:
        #         q.put((l.val, l))
        # while not q.empty():
        #     val, node = q.get()
        #     point.next = ListNode(val)
        #     point = point.next
        #     node = node.next
        #     if node:
        #         q.put((node.val, node))
        # return head.next
        res = []
        for idx, l in enumerate(lists):
            if l:
                res.append((l.val, idx, l))
        heapq.heapify(res)

        while res:
            val, idx, node = heapq.heappop(res)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(res, (node.val, idx, node))
        return head.next


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(3, ListNode(4, ListNode(5)))
    list3 = ListNode(2, ListNode(3, ListNode(6)))
    lists = [list1, list2, list3]

    print(Solution().mergeKLists(lists))
