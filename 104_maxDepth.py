# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        use recursion to return the depth of left and right leaves
        """
        return 0 if root is None else 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))



