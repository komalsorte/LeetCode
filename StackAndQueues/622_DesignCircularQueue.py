"""
LeetCode - Medium
"""

"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.queue = [''] * self.k
        self.isQueueEmpty = True
        self.isQueueFull = False
        self.elements = 0
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isQueueFull:
            return False
        else:
            if self.tail == self.k - 1:
                self.tail = 0
            else:
                self.tail += 1
            self.queue[self.tail] = value
            self.elements += 1
            if self.elements == self.k:
                self.isQueueFull = True
                self.isQueueEmpty = False
            elif self.elements == 0:
                self.isQueueFull = False
                self.isQueueEmpty = True
            else:
                self.isQueueFull = False
                self.isQueueEmpty = False
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isQueueEmpty:
            return False
        else:
            self.queue[self.head] = ''
            self.head += 1
            self.elements -= 1
            if self.elements == self.k:
                self.isQueueFull = True
                self.isQueueEmpty = False
            elif self.elements == 0:
                self.isQueueFull = False
                self.isQueueEmpty = True
            else:
                self.isQueueFull = False
                self.isQueueEmpty = False
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isQueueEmpty:
            return -1
        else:
            return self.queue[self.head]



    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isQueueEmpty:
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.isQueueEmpty

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.isQueueFull

# Your MyCircularQueue object will be instantiated and called as such:
#
if __name__ == '__main__':
    k = 5
    value = 1
    obj = MyCircularQueue(k)
    param_1 = obj.enQueue(1)
    param_1 = obj.enQueue(2)
    param_1 = obj.enQueue(3)
    param_1 = obj.enQueue(4)
    param_1 = obj.enQueue(5)
    param_1 = obj.enQueue(6)
    param_2 = obj.deQueue()
    param_1 = obj.enQueue(6)
    aram_2 = obj.deQueue()
    aram_2 = obj.deQueue()
    aram_2 = obj.deQueue()
    aram_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()