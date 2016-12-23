'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            def reverseList(head):
                dummy = ListNode(0)
                while head:
                    dummy.next, head.next, head = head, dummy.next, head.next
                return dummy.next

            hare = torte = head
            while hare.next and hare.next.next:
                torte = torte.next
                hare = hare.next.next
            rev = reverseList(torte.next)
            torte.next = None
            isEven = True
            res = ListNode(0)
            copy = head
            while copy or rev:
                if isEven == True:
                    res.next = copy
                    copy = copy.next
                    isEven = False
                elif isEven == False:
                    res.next = rev
                    rev = rev.next
                    isEven = True
                res = res.next
            return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)
    #head.next.next.next.next.next = ListNode(6)
    #head.next.next.next.next.next.next = ListNode(7)
    res = Solution().reorderList(head)
    while res:
        print(res.val)
        res = res.next
