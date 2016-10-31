'''
284. Peeking Iterator

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Hint:

1. Think of "looking ahead". You want to cache the next element.
2. Is one variable sufficient? Why or why not?
3. Test your design with call order of peek() before next() vs next() before peek().
4. For a clean implementation, check out Google's guava library source code.

*Follow up: How would you extend your design to be generic and work with all types, not just integer?
'''
# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._iter = iter(nums)
        try:
            self.copy = next(self._iter) # int
        except:
            self.copy = None

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.copy is not None

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        temp = self.copy
        try:
            self.copy = next(self._iter) # int
        except:
            self.copy = None
        return temp

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        if self._iter.hasNext(): # self._iter is pointing at the next ppl
            self.copy = self._iter.next()
        else:
            self.copy = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        save a copy so that you don't really go to the next one when peeking
        """
        return self.copy

    def next(self):
        """
        :rtype: int
        """
        temp = self.copy
        if self._iter.hasNext(): # self._iter is pointing at the next ppl
            self.copy = self._iter.next()
        else:
            self.copy = None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.copy is not None

if __name__ == '__main__':
    nums = [1, 2, 3]
    it = Iterator(nums)
    assert it.hasNext()
    assert it.next() == 1
    assert it.hasNext()
    assert it.next() == 2
    assert it.hasNext()
    assert it.next() == 3
    assert not it.hasNext()
    it = Iterator(nums)
    p = PeekingIterator(it)
    assert p.hasNext()
    assert p.next() == 1
    assert p.hasNext()
    assert p.peek() == 2
    assert p.next() == 2
    assert p.hasNext()
    assert p.next() == 3
    assert not p.hasNext()

