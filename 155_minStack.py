class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        keep a saperate array to keep only desending elements (the last one is always the smallest)
        """
        self.__data, self.__minData = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__data.append(x)
        self.__minData.append(x if not self.__minData or x < self.__minData[-1] else self.__minData[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.__data.pop()
        self.__minData.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.__data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__minData[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
