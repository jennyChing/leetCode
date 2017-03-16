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
        copy = odd = curr = head
        currSteps = 0
        while odd:
            print(currSteps)
            for _ in range(currSteps + 2):
                try:
                    odd = odd.next
                except:
                    break
            if not odd:
                break
            try:
                tail = odd.next
            except:
                tail = None
            even = curr.next
            odd.next = even
            for _ in range(currSteps):
                even = even.next
            even.next = tail
            curr.next = odd

            print("odd node ", odd.val)
            curr = curr.next
            currSteps += 1
        return copy

# second attempt
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # idea: keep pointer at odd, walk every 2 + n nodes as curr => Skip curr and append it after odd
        if not head or not head.next or not head.next.next:
            return head
        odd, pre, curr = head, head.next, head.next.next
        while curr:
            insert = ListNode(curr.val)
            insert.next = odd.next # insert odd node value
            odd.next = insert
            if curr.next and curr.next.next:
                walk_to_next_odd = curr.next.next # walk 2 nodes to next odd node
            else:
                pre.next = curr.next # skip curr
                break
            pre.next = curr.next # skip curr
            curr = walk_to_next_odd # update curr to next odd node
            odd = odd.next
            pre = pre.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)
    #head.next.next.next.next.next = ListNode(6)
    #head.next.next.next.next.next.next = ListNode(7)
    #head.next.next.next.next.next.next.next = ListNode(8)
    res = Solution().oddEvenList(head)
    while res:
        print(res.val)
        res = res.next


