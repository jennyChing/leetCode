# Complete the function below.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNodes(self, list, x):
        pre = curr = dummy = ListNode(0)
        pre.next, curr.next = list, list
        curr = curr.next
        while curr:
            if curr.val > x:
                print(curr.val, pre.val)
                if curr.next:
                    pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = Solution().removeNodes(head, 2)
