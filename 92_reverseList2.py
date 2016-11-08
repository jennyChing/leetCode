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
# Helper function copy from #206 reverse List to reverse the segment of len k from head and connect new tail:
        def reverseList(head, k):
            prev = ListNode(0)
            prev.next = head
            node = head
            for _ in range(k): # reversing k nodes
                temp = head
                head = head.next
                temp.next = prev
                prev = temp
            node.next = head # head is now on the n position
            return prev

        if m == n:
            return head
        # location m using for loop, not while loop + variable 'count'
        prev = ListNode(0)
        prev.next = head
        res = prev
        for _ in range(m - 1):
            prev = prev.next

        prev.next = reverseList(prev.next, n - m + 1)
        return res.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = Solution().reverseBetween(head, 2, 4)
    while res:
        print(res.val)
        res = res.next
