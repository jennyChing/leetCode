'''
206. Reverse Linked List

Reverse a singly linked list.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        insert nodes into new LinkedList (FILO)
        """
        def AppendNode(curr, data): # insert a node at the front
           temp = ListNode(data)
           temp.next = curr
           return temp
        curr = ListNode(head.val)
        head = head.next
        while head:
            curr = AppendNode(curr, head.val)
            head = head.next
        return curr

    def reverseList_2(self, head):
	dummy = ListNode(0)
        if not head or not head.next:
            return head
        curr = head
        while curr.next:
            curr.next = dummy.next
            dummy.next = curr
            curr = next
        curr.next = dummy.next
        dummy.next = curr
        return dummy.next

    def reverseList_refer(self, head):
	dummy = ListNode(0)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

if __name__ == '__main__':
   head = ListNode(5)
   head.next = ListNode(1)
   head.next.next = ListNode(3)
   res = Solution().reverseList_2(head)
   while res:
       print(res.val)
       res = res.next

