# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
         if head == None:
             return head
         curr = ListNode(head.val)
         head = head.next
         while head:
             curr = Solution().AppendNode(curr, head.val)
             head = head.next
         return curr
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use an array to store the values?? overkill...
        # copy a reversed linkedList and compare the first half of it
        reversed = Solution().reverseList(head)
        while head:
            if reversed.val != head.val:
                return False
            reversed = reversed.next
            head = head.next
        return True

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        def reverse(head):
            dummy = ListNode(0)
            while head:
                dummy.next, head.next, head = head, dummy.next, head.next
            return dummy.next

        hare = tort = head
        while hare.next and hare.next.next:
            hare = hare.next.next
            tort = tort.next
        reverse = reverse(tort.next)
        while reverse:
            print(reverse.val, head.val)
            if head.val != reverse.val:
                return False
            head, reverse = head.next, reverse.next
        return True

