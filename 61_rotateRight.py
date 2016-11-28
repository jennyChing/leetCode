'''
61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
	if not head:
            return None

        if head.next == None:
            return head
        if k == 0:
            return head
        curr = head
        lenOfList = 1 # default value
        # step one:
        while curr.next:
            curr = curr.next
            lenOfList += 1
        rotateTimes = k % lenOfList
        if k == 0 or rotateTimes == 0:
            return head

        # step two:
        slow, fast = head, head
        for _ in range(rotateTimes):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        head = new_head
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = Solution().rotateRight(head, 1)
    while res:
        print(res.val)
        res = res.next
