__author__ = "Komal Atul Sorte"
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.

"""

from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = deque()
        self.minList = list()
        self.minimum = float('inf')

    def push(self, x):
        self.minStack.appendleft(x)  # O(1)
        if self.minimum > x:
            self.minimum = x
            self.minList.append(x)
        else:
            self.minList.append(self.minimum)

    def pop(self):
        if len(self.minStack) != 0:
            ele = self.minStack[0]
            self.minStack.popleft()  # O(1)
            self.minList.pop()  # O(1)
            if len(self.minList) == 0:  # O(1)
                self.minimum = float('inf')
            else:
                self.minimum = self.minList[len(self.minList) - 1]

    def top(self):
        if len(self.minStack) != 0:
            return self.minStack[0]  # O(1)

    def getMin(self):
        if len(self.minStack) != 0:
            return self.minimum  # O(1)
        return



# Your MinStack object will be instantiated and called as such:
obj2 = MinStack()
#["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
obj2.push(2147483646)
obj2.push(2147483646)
obj2.push(2147483647)
print(obj2.top())
obj2.pop()
print(obj2.getMin())
obj2.pop()
print(obj2.getMin())
obj2.pop()
obj2.push(2147483647)
print(obj2.top())
print(obj2.getMin())
obj2.push(2147483648)
print(obj2.top())
print(obj2.getMin())
obj2.pop()
print(obj2.getMin())



obj = MinStack()
obj.push(1222)
obj.push(11)
obj.push(5)
obj.push(1)
obj.push(5)
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

obj1 = MinStack()
obj1.push(2)
obj1.push(0)
obj1.push(-3)
print(obj1.minList)
print(obj1.getMin())
obj1.pop()
print(obj1.minList)
print(obj1.top())
print(obj1.minList)
print(obj1.getMin())
