# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # [idea] use currLevel stack to record visited nodes. While currLevel: pop 1 node and append child to nextLevel
        if not root:
            return []
        res = []
        currLevel = collections.deque([root])
        while currLevel:
            nextLevel, curr_vals = collections.deque([]), []
            while currLevel:
                root = currLevel.popleft()
                curr_vals.append(root.val)
                if root.left:
                    nextLevel.append(root.left)
                if root.right:
                    nextLevel.append(root.right)
            res.append(curr_vals)

            currLevel = nextLevel
        return res
