'''
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, l, r): # merge 2 sorted lists into one
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l # swap the list to sort
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else: # do the merging here (pre is before l needed to be swap, tmp is after targeted r)
                nxt = pre.next
                tmp = r.next
                pre.next = r
                r.next = nxt
                r = tmp
            pre = pre.next
        pre.next = l or r
        return head

    def sortList(self, head): # split list into 2 parts recursively and merge them in to sorted order
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: # at least has 2 nodes
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # create a new List for the right part
        slow.next = None
        # recursively cut the 2 parts into pairs
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

# split head list into 2 parts

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(2)
    res = Solution().sortList(head)
    while res:
        print(res.val)
        res = res.next
