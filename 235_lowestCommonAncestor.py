# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        trick: always default the same side p < root < q (swap it if not) and move down root
        """
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        while not p.val <= root.val <= q.val: # not the correct root then move down
            root = root.left if root.val > q.val else root.right
        return root
