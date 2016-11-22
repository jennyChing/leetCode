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
        dummy = ListNode(0)
        dummy.next = head
        curr = part2_start = head
        cnt = 0
        # step one:
        while curr:
            curr = curr.next
            cnt += 1
            print(cnt)
        # step two:
        new_h = head
        for _ in range(cnt - k):
            new_h = new_h.next
        part2_end = new_h
        new_h = new_h.next
        if not new_h:
            return head
        part1_end = new_h
        print(part1_end.val)
        for _ in range(k - 1):
            part1_end = part1_end.next
        dummy.next = new_h
        part1_end.next = head
        part2_end.next = None
        return new_h

if __name__ == "__main__":
    head = ListNode(1)
    #head.next = ListNode(2)
    #head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)
    res = Solution().rotateRight(head, 1)
    while res:
        print(res.val)
        res = res.next
