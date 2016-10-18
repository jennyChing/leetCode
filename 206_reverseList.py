'''
206. Reverse Linked List

Reverse a singly linked list.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def AppendNode(self, head, data):
       temp = ListNode(data)
       temp.next = head
       return temp
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        insert nodes into new LinkedList (FILO)
        """
        curr = ListNode(head.val)
        head = head.next
        while head:
            curr = Solution().AppendNode(curr, head.val)
            head = head.next
        return curr
if __name__ == '__main__':
   head = ListNode(5)
   head.next = ListNode(1)
   head.next.next = ListNode(3)
   res = Solution().reverseList(head)
   while res:
       print(res.val)
       res = res.next
