# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            if root: # go as left as you can and append each node to the stack
                stack.append(root)
                root = root.left
            else: # when you can't go left, pop the stack to get the most recently added node
                print(stack[-1].val)
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    res = Solution().inorderTraversal(root)
    print(res)
