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
    def sortedListToBST(self, head):
        """
        :type nums: List[int]
        :rtype: TreeNode
        careful not to pass the whole linkedlist into left root.left recursion
        """
        if not head:
            return None
        fast = slow = head
        dummy = copy = ListNode(0)

# keep a copy that records the part that should be pass to the left recursive
        copy.next = head

        # find mid at pointer slow: be sure to check both fast and fast.next
        while fast and fast.next:
            copy = copy.next
            slow = slow.next
            fast = fast.next.next

# keep a copy of value from dummy.next to the one before slow (left part of the linkedList
        copy.next = None
        root = TreeNode(slow.val)
        root.left, root.right = self.sortedListToBST(dummy.next), self.sortedListToBST(slow.next)
        return root
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

