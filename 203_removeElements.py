'''
203. Remove Linked List Elements  QuestionEditorial Solution

Remove all elements from a linked list of integers that have value val.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while head:
            if head.val != val:
                print(curr.val, head.val)
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
            else:
                head = head.next
        return dummy.next
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    #head.next.next = ListNode(3)
    #head.next.next.next = ListNode(5)
    res = Solution().removeElements(head, 2)
    while res:
        print(res.val)
        res = res.next

