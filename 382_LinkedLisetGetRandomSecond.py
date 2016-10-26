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
        self.__head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = self.__head.val
        curr, n = self.__head.next, 1
        # Key concept: Reservoir sampling (many application!)
        while curr:
            # randrange: 0 ~ n - 1
            n += 1
            res = curr.val if random.randrange(n) == 0 else res
            print("random :", n, res)
            curr = curr.next
        return res

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    obj = Solution(head)
    param_1 = obj.getRandom()
    print(param_1)

# Your Solution object will be instantiated and called as such:
