'''
341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
'''

class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """


   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]] # record the current nestedList in use and the next free element of it with a stack

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        currList, idx = self.stack[-1]
        self.stack[-1][1] += 1
        return currList[idx].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack: # when the currList on top of the stack is a list, read it from the stack and flatten it
            currList, idx = self.stack[-1]
            if len(currList) == idx: # no available elements left in the currList
                self.stack.pop()
            else:
                a = currList[idx]
                if a.isInteger(): # next available element is an integer
                    return True
                self.stack[-1][1] += 1 # next available element is a list
                self.stack.append([a.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
if __name__ == '__main__':
    nestedList = NestedInteger()
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)



