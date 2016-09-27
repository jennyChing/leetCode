'''
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def __get_len(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        def __move_steps(head, step):
            for _ in range(step):
                head = head.next
            return head
        len_a, len_b = __get_len(headA), __get_len(headB)
        if len_a > len_b:
            headA = __move_steps(headA, len_a - len_b)
        else:
            headB = __move_steps(headB, len_b - len_a)
        while headA and headB and headA != headB:
            headA, headB = headA.next, headB.next # keep moving down to end of list or intersect
        return headA

if __name__ == '__main__':

