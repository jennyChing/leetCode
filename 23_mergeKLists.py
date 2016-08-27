import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        param is a number of list
        return a ListNode
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_list, heap = [], []
        #if lists == []:
         #   return []

        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        while heap:
# keep a min-heap for sorting
            sorted_list.append(heapq.heappop(heap))
        print(sorted_list)

if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)
    s.mergeKLists([list1, list2])

