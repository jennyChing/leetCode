'''
142. Linked List Cycle II  QuestionEditorial Solution

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return
        tort, hare = head, head
        while hare.next and hare.next.next:
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
            #Intuitive method:
                tort = tort.next
                cycle_len = 1
                while tort != hare:
                    tort = tort.next
                    cycle_len += 1
                tort = hare = head
                steps = 0
                while steps <= cycle_len:
                    tort = tort.next
                    steps += 1
                while tort != head:
                    tort = tort.next
                    hare = hare.next
                return tort.val

            # textbook method:
       #         tort = head
       #         while tort != head:
       #             tort = tort.next
       #             hare = hare.next
       #         return tort.val
        return
if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = head
    print(Solution().detectCycle(head))
