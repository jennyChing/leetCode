'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :rtype: ListNode
        KEY: linkedlist munipulation
        """
# not enough: need both smallNode and bigNode pointer
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head

# find the first element >= x:
        bigpre, bigcur = dummy, head
        while bigcur:
            if bigcur.val >= x:
                break
            bigpre = bigcur
            bigcur = bigcur.next
        if not bigcur:
            return head

# find the value less then x:
        smallpre, smallcur = None, bigcur
        while smallcur:
            if smallcur.val < x:
                pnext = smallcur.next
                bigpre.next = smallcur
                smallcur.next = bigcur
                smallpre.next = pnext
                bigpre = smallcur
                smallcur = pnext

            else:
                smallpre = smallcur
                smallcur = smallcur.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(2)
    head.next = ListNode(1)
    #head.next.next = ListNode(3)
    #head.next.next.next = ListNode(2)
    #head.next.next.next.next = ListNode(5)
    #head.next.next.next.next.next = ListNode(2)
    res = Solution().partition(head, 3)
    while res:
        print(res.val)
        res = res.next

