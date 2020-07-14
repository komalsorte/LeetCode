__author__ = "Komal Atul Sorte"
"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
 

Example:

Input: 
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:  
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
 
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
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None:
            return -1
        else:
            current = self.head
            index -= 1
            val = current.data
            if index == -1:
                return val
            while current.next is not None:
                current = current.next
                index -= 1
                if index == -1:
                    return current.data
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        current = Node(val)
        if self.head is None:
            self.head = current
        else:
            current.next = self.head
            self.head = current

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if self.head is None and index == 0:
            self.head = node
        if index == 0:
            node.next = self.head
            self.head = node
        elif self.head is not None:
            current = self.head
            while index != 1 and current.next is not None:
                current = current.next
                index -= 1
            if index == 1:
                node.next = current.next
                current.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is not None and index == 0:
            self.head = self.head.next
        elif self.head is not None:
            current = self.head
            previous = None
            while index != 0 and current.next is not None:
                previous = current
                current = current.next
                index -= 1
            if index == 0:
                previous.next = current.next
                current.next = None


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    ll = LinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    print(ll.get(1))
    ll.deleteAtIndex(1)
    print(ll.get(1))

    # ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
    # [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    ll1 = LinkedList()
    ll1.addAtHead(7)
    ll1.addAtHead(2)
    ll1.addAtHead(1)
    ll1.addAtIndex(3, 0)
    ll1.deleteAtIndex(2)
    ll1.addAtHead(6)
    ll1.addAtTail(4)
    print(ll1.get(4))
    ll1.addAtHead(4)
    ll1.addAtIndex(5, 0)
    ll1.addAtHead(6)

    # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    # [[],[1],[3],[1,2],[1],[0],[0]]
    ll2 = LinkedList()
    ll2.addAtHead(1)
    ll2.addAtTail(3)
    ll2.addAtIndex(1, 2)
    print(ll2.get(1))
    ll2.deleteAtIndex(0)
    print(ll2.get(0))

    # ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
    # [[],[0,10],[0,20],[1,30],[0]]
    ll3 = LinkedList()
    ll3.addAtIndex(0, 10)
    ll3.addAtIndex(0, 20)
    ll3.addAtIndex(1, 30)
    print(ll3.get(0))