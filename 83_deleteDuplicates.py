'''
83. Remove Duplicates from Sorted List  QuestionEditorial Solution

Given a sorted linked list, delete all duplicates such that each element appear only once.
'''
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
        unique = set()
        curr = copy = ListNode(0)
        while head:
            if head.val not in unique:
# deal with the last node if duplicated (or create a new LinkedList add nodes only if unique)
                print(unique, curr.val, head.val)
                curr.next = ListNode(head.val)
                curr = curr.next
            unique.add(head.val)
            head = head.next
        return copy.next


    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # key: deal with the last node if duplicated using pre jump to next
        memo = set()
        copy = head
        pre = ListNode(0)
        pre.next = head
        while head:
            if head.val in memo:
                pre.next = head.next # pre jump to next node, pre stays same
            else: # the head.val is unique
                memo.add(head.val)
                pre = pre.next
            head = head.next # move head forward
        return copy

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    res = Solution().deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next


