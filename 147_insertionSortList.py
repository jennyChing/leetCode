'''
147. Insertion Sort List

Sort a linked list using insertion sort.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        KEY: linkedlist munipulation
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            # swap = curr.next (don't need the swap value, just initiate curr.next)
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next

                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(2)
    head.next = ListNode(5)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(8)
    res = Solution().insertionSortList(head)
    while res.next:
        print(res.val)
        res = res.next

