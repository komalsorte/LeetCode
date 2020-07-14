__author__ = "Komal Atul Sorte"
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    visited = dict()

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        original_node = head
        current = Node(original_node.val)
        new_head = current
        self.visited[original_node] = current
        while original_node.next is not None:
            if original_node.next in self.visited:
                current.next = self.visited[original_node.next]
            else:
                current.next = Node(original_node.next.val)
                self.visited[original_node.next] = current.next
            if original_node.random in self.visited:
                current.random = self.visited[original_node.random]
            else:
                if original_node.random is not None:
                    current.random = Node(original_node.random.val)
                    self.visited[original_node.random] = current.random
                else:
                    current.random = None

            current = current.next
            original_node = original_node.next
        if original_node.random in self.visited:
            current.random = self.visited[original_node.random]
        else:
            if original_node.random is not None:
                current.random = Node(original_node.random.val)
                self.visited[original_node.random] = current.random
            else:
                current.random = None
        return new_head


