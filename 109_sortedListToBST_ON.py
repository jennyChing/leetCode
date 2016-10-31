'''
109. Convert Sorted List to Binary Search Tree

Given an list where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __direct_build(self, start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
    # finish building left subtree first
        left_subtree = self.__direct_build(start, mid)
        root = TreeNode(self._head.val)
        root.left = left_subtree
        self._head = self._head.next
    # build right tree here
        root.right = self.__direct_build(mid + 1, end)
    # travese to get the mid first
        return root

    def sortedListToBST(self, head):
        self._head = head
        """
        :type nums: List[int]
        :rtype: TreeNode
        traverse only once to implement te O(n) solution
        """
        start, end = 0, 0
        while head:
            head = head.next
            end += 1
        return self.__direct_build(start, end)

if __name__ == '__main__':
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(3)
   head.next.next.next = ListNode(4)
   head.next.next.next.next = ListNode(5)
   res = Solution().sortedListToBST(head)
   assert res.val == 3
   assert res.left.val == 2
   assert res.right.val == 5
   assert res.left.left.val == 1
   assert res.right.left.val == 4

