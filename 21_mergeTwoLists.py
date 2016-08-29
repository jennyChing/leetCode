import heapq
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
        sorted_list = []
        if l1 == []:
            return l2
        elif l2 == []:
            return l1

        while l1.next != None and l2.next != None:
            print(l1.val, l2.val)
            if l1.val < l2.val:
                sorted_list.append(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                sorted_list.append(l2.val)
                l2 = l2.next
            else:
                print(sorted_list)
                sorted_list.append(l1.val)
                sorted_list.append(l2.val)
                l2 = l2.next
                l1 = l1.next
        print(sorted_list)
        if l1.val > l2.val:
            sorted_list.append(l2.val)
            sorted_list.append(l1.val)
        else:
            sorted_list.append(l1.val)
            sorted_list.append(l2.val)
        print(sorted_list)

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    list2 = ListNode(2)
    list2.next = ListNode(5)
    list2.next.next = ListNode(6)
    s.mergeTwoLists(list1, list2)

