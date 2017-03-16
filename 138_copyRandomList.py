'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

import collections
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        visited = collections.defaultdict(lambda: RandomListNode(0))
        visited[None] = None
        cur = head
        while cur:
            print(visited[cur].label)
            visited[cur].label = cur.label
            print(visited[cur].label)
            visited[cur].next = visited[cur.next]
            visited[cur].random = visited[cur.random]
            cur = cur.next
        return visited[head]
if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.random = RandomListNode(3)
    head.next.next = head.random
    res = Solution().copyRandomList(head)
