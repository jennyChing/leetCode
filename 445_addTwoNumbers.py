'''
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def __reverse(head):
            dummy = ListNode(0)
            while head: # insert nums at the front of dummy linkedList
                dummy.next, head.next, head = head, dummy.next, head.next
            return dummy.next

        def __insert_node(data):
            tail = dummy.next
            dummy.next = ListNode(data) # insert to front
            dummy.next.next = tail

        l1, l2 = __reverse(l1), __reverse(l2)
        dummy, carry = ListNode(0), 0
        while l1 and l2:
            __insert_node((l1.val + l2.val + carry) % 10) # insert to front
            carry = 1 if l1.val + l2.val + carry > 9 else 0
            l1, l2 = l1.next, l2.next
        while l1:
            __insert_node((l1.val + carry) % 10)
            carry = 1 if l1.val + carry > 9 else 0
            l1 = l1.next
        while l2:
            __insert_node((l2.val + carry) % 10)
            carry = 1 if l2.val + carry > 9 else 0
            l2 = l2.next

        if carry == 1:
            __insert_node(1)
        return dummy.next

    def addTwoNumbers_refer(self, l1, l2): # not using reverse
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def __insert_node(data):
            tail = dummy.next
            dummy.next = ListNode(data) # insert to front
            dummy.next.next = tail

        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        dummy, carry = ListNode(0), 0
        while s1 or s2:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            s = a + b + carry
            __insert_node(s % 10)
            carry = s // 10
        if carry == 1:
            __insert_node(1)
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = Solution().addTwoNumbers_refer(l1, l2)
    while res:
        print(res.val)
        res = res.next

