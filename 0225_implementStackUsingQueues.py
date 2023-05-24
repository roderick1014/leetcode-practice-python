# 0225 - Implement Stack using Queues

'''
    Question:
        Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

        Implement the MyStack class:

        void push(int x) Pushes element x to the top of the stack.
        int pop() Removes the element on the top of the stack and returns it.
        int top() Returns the element on the top of the stack.
        boolean empty() Returns true if the stack is empty, false otherwise.
        
        Notes:

        You must use only standard operations of a queue, 
        which means that only push to back, peek/pop from front, 
        size and is empty operations are valid.
        
        Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

'''

import collections

class MyStack(object):

    def __init__(self):
        # Standard double-ended queue is the requirement of the question.
        self.queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        queue_len = len(self.queue)
        while queue_len > 1:
            self.queue.append(self.queue.popleft())
            queue_len -= 1        

    def pop(self):
        """
        :rtype: int
        """
        
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    # x = []
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_3 = obj.top()
    print(param_3)
    param_2 = obj.pop()
    print(param_2)
    param_4 = obj.empty()
    print(param_4)