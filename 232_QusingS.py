class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.enq = [] # one stack for appending
        self.deq = [] # and one stack for deleting

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.enq.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.deq == []:
            while self.enq != []:
                self.deq.append(self.enq.pop())
        self.deq.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.deq(0)

    def empty(self):
        """
        :rtype: bool
        """
        if self.enq or self.deq:
            return False
        return True
if __name__ == '__main__':
    q = Queue()
    q.push(1)
    print(q)
    q.pop()
    print(q)

