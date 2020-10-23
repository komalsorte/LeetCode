"""
LeetCode - Easy
"""
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""

from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque(maxlen=size)
        self.elements = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.elements == self.queue.maxlen:
            self.sum = self.sum*self.elements - self.queue[0] + val
            self.sum = self.sum/self.elements
        else:
            self.sum = (self.sum * self.elements + val)
            self.elements += 1
            self.sum = self.sum/self.elements
        self.queue.append(val)
        return self.sum

# Your MovingAverage object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MovingAverage(3)
    param_1 = obj.next(1)
    param_1 = obj.next(2)
    param_1 = obj.next(3)
    param_1 = obj.next(4)
    print(param_1)