# 0155 - Min Stack

'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
'''

# Solution 1 - Using tuple to store the min val.
class MinStack(object):
    def __init__(self):
            """
            initialize your data structure here.
            """
            self.stack= []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(x,self.stack[-1][1])))
            # This line records the minimal val in a tuple
            # Example: push(1) -> push(3) -> push(0) -> push(4)
            #           (1, 1) -> (3,1) -> (0, 0) -> (4, 0)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        else:
            return None

'''
    Solution 2 - My Solution
'''

from collections import deque

class MinStack(object):

    def __init__(self):
        self.stack = deque()
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


