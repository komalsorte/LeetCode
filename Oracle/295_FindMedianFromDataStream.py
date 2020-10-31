"""
LeetCode - Hard
"""
import heapq

"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []  # all small numbers - ultimately pop the largest of all small numbers
        heapq.heapify(self.max_heap)
        self.min_heap = []  # pops smallest - hence all large numbers
        heapq.heapify(self.min_heap)
        self.num_elements = 0

    def addNum(self, num: int) -> None:
        if len(self.max_heap) < len(self.min_heap):
            min_heap_top = heapq.heappushpop(self.min_heap, num)
            heapq.heappush(self.max_heap, -1 * min_heap_top)
        else:
            heapq.heappush(self.min_heap, num)
        self.num_elements += 1


    def findMedian(self) -> float:
        if self.num_elements % 2 == 0:
            median = (self.min_heap[0] + (self.max_heap[0]) * -1) / 2
        else:
            if len(self.min_heap) < len(self.max_heap):
                median = self.max_heap[0] * -1
            else:
                median = self.min_heap[0]
        return median


# Your MedianFinder object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(6)
    obj.addNum(2)
    obj.addNum(4)
    obj.addNum(3)
    obj.addNum(5)
    obj.addNum(1)
    param_2 = obj.findMedian()
    print(param_2)

    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())

    obj = MedianFinder()
    obj.addNum(-1)
    print(obj.findMedian())
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    print(obj.findMedian())
    obj.addNum(-5)
    print(obj.findMedian())

