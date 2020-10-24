"""
LeetCode - Easy
"""
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
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minimum_stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minimum_stack) == 0:
            self.minimum_stack.append(x)
        else:
            if self.minimum_stack[-1] >= x:
                self.minimum_stack.append(x)

    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.minimum_stack[-1] == self.top():
                self.minimum_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.push(1)
    obj.push(-4)
    obj.push(2)
    obj.push(10)

    print(obj.getMin())
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
