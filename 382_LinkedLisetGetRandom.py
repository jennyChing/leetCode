import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.count = 0
        copy = head
        while copy:
            self.count +=1
            copy = copy.next
        print(self.count)

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.count == 1:
            return self.head
        n = random.randint(0, self.count - 1)
        print(n)
        for _ in range(n):
            self.head = self.head.next
        return self.head.val
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    obj = Solution(head)
    param_1 = obj.getRandom()
    print(param_1)

# Your Solution object will be instantiated and called as such:
