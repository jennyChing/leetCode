# Definition for a binary tree node.
# Given a binary tree, return the preorder traversal of its nodes' values.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [root]
        while stack:
            curr = stack.pop() # the most recent added node is the new current
            if curr: # start traversal from the first level
                stack.append(curr.right) # push right first, traverse later
                stack.append(curr.left) # push left later, traverse first
                res.append(curr.val)
        return res
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    res = Solution().preorderTraversal(root)
    print(res)
