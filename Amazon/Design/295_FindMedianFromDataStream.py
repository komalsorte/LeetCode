__author__ = "Komal Atul Sorte"
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
        self.numList = list()

    def addNum(self, num: int) -> None:
        self.numList.append(num)
        self.numList = sorted(self.numList)

    def findMedian(self) -> float:
        if len(self.numList) != 0:
            if len(self.numList) % 2 == 0:
                median = self.numList[len(self.numList) // 2] + self.numList[len(self.numList) // 2 - 1]
                median = median / 2
                return median
            else:
                median = self.numList[len(self.numList) // 2]
                return median
        return


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
obj.addNum(3)
param_2 = obj.findMedian()

# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

obj2 = MedianFinder()
obj2.addNum(6)
print(obj2.findMedian())
obj2.addNum(10)
print(obj2.findMedian())
obj2.addNum(2)
print(obj2.findMedian())
obj2.addNum(6)
print(obj2.findMedian())
obj2.addNum(5)
print(obj2.findMedian())
obj2.addNum(0)
print(obj2.findMedian())
obj2.addNum(6)
print(obj2.findMedian())
obj2.addNum(3)
print(obj2.findMedian())
obj2.addNum(1)
print(obj2.findMedian())
obj2.addNum(0)
print(obj2.findMedian())
obj2.addNum(0)
