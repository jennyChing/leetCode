# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [root]
        while stack:
            curr = stack.pop()
            if curr:
                stack.append(curr.right)
                stack.append(curr.left)
                res.append(curr.val)
        return res

# recursive: root > left > right
    def preorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        res.append(root.val)
        if root.left:
            res += self.preorderTraversal(root.left)
        if root.right:
            res += self.preorderTraversal(root.right)
        return res
