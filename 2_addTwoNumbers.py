'''
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Step1: walk to end of list
        l1_stack, l2_stack = [], []
        l1_len, l2_len = 0, 0
        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next
            l1_len += 1
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next
            l2_len += 1

        while l1_len > l2_len:
            l2_stack.append(0)
            l1_len -= 1
        while l1_len < l2_len:
            l1_stack.append(0)
            l2_len -= 1
        #print(l1_stack, l2_stack)

        # Step2: compute sum and append to the res list
        isCarry = 0
        dummy = res = ListNode(0)
        while l1_stack:
            l1_curr = l1_stack.pop(0)
            l2_curr = l2_stack.pop(0)
            #print(l1_curr, l2_curr, isCarry)
            res.next = ListNode((l1_curr + l2_curr + isCarry) % 10)
            res = res.next
            isCarry = 1 if isCarry + l1_curr + l2_curr > 9 else 0
        #print("carry", isCarry)
        if isCarry == 1:
            res.next = ListNode(1)
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = Solution().addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next


