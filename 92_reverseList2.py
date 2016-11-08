'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        cnt = 0 # location m and n node
        curr = dummy = ListNode(0)
        curr.next = head
        curr = curr.next
        while curr:
            if cnt == m:
                beforeM = curr
                afterM = curr.next.next
            elif cnt == n:
                beforeN = curr
                afterN = curr.next.next
            curr = curr.next
            cnt += 1
            #0~beforeM + N + afterM + afterM~beforeN + M + afterN
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = Solution().reverseBetween(head, 2, 4)
