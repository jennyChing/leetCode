'''
328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even = ListNode(0), ListNode(0)
        iters, idx = [odd, even], 0
# use array iters to store the two linkedlist and append the curr node to odd or even based on idx is 0 or 1 (binary complement)
        while head:
            iters[idx].next = head
            iters[idx] = iters[idx].next
            print("before binary complement :", idx)
            idx ^= 1
            print("after binary complement :", idx)
            head = head.next
        # connent even linkedList to the end of odd linkedList
        iters[0].next = even.next
        iters[1].next = None
        return odd.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    res = Solution().oddEvenList(head)
    while res:
        print(res.val)
        res = res.next


