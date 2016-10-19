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
        """
        if not head:
            return None
        dummy = fast = slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            print(slow.val, fast.val)
        root = TreeNode(slow.val)
        #root.left, root.right = self.sortedListToBST(dummy), self.sortedListToBST(slow.next)
        return root
if __name__ == '__main__':
   head = ListNode(1)
   head.next = ListNode(2)
   head.next.next = ListNode(3)
   head.next.next.next = ListNode(4)
   head.next.next.next.next = ListNode(5)
   res = Solution().sortedListToBST(head)
