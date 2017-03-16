'''
24. Swap Nodes in Pairs  QuestionEditorial Solution

Given a linked list, swap every two adjacent nodes and return its head.
'''

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs_refer(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            next_1, next_2, next_3 = curr.next, curr.next.next, curr.next.next.next
            curr.next = next_2
            next_2.next = next_1
            next_1.next = next_3
            curr = next_1
        return dummy.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = dummy = ListNode(0)
        tail.next = head
        while tail and tail.next:
# skip the odd node and store as oddNode
            oddNode = tail.next
            tail.next = tail.next.next
            tail = tail.next
# link back the odd node
            tail.next = oddNode
            tail = tail.next
        return dummy

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    res = Solution().swapPairs_refer(head)
    while res:
        print(res.val)
        res = res.next


