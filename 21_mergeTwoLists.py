class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        param is two lists
        return a ListNode
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tail = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1 == None:
            tail.next = l2
        else:
            tail.next = l1
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    list2 = ListNode(2)
    list2.next = ListNode(5)
    list2.next.next = ListNode(6)
    res = s.mergeTwoLists(list1, list2)
    while res != None:
        print(res.val)
        res = res.next

