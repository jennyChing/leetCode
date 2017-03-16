# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # better way: head walk n first, then dummy and head walk till head reach end (dummy walked len - n steps) and skip n
        len = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for _ in range(n):
            head = head.next
        while head:
            head, curr = head.next, curr.next
        curr.next = curr.next.next # skip nth node
        return dummy.next
