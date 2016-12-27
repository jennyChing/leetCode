'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prenode = ListNode(0)
        prenode.next = curr = head
        isDup = False
        while curr:
            if curr.next and curr.val == curr.next.val:
                isDup = True
            else:
                if isDup == True:
                    prenode.next = curr.next
                else:
                    prenode = curr
                isDup = False
            curr = curr.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    #head.next.next.next = ListNode(2)
    #head.next.next.next.next = ListNode(4)
    res = Solution().deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next

