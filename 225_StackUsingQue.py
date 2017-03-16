class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        tmp = self.q1.pop(0)
        self.q1, self.q2 = self.q2, []
        return tmp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[-1] # last element (most recent added) in q1 is the top of the stack

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
