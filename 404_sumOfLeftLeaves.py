'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def __directed_dfs(root):
            if root.left and not root.left.left and not root.left.right:
                res[0] += root.left.val
            if root.left:
                __directed_dfs(root.left)
            if root.right:
                __directed_dfs(root.right)
        res = [0]
        __directed_dfs(root)
        return res[0]

    def more_consice_dfs(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.more_consice_dfs(root.right)
        return self.more_consice_dfs(root.left) + self.more_consice_dfs(root.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = Solution().sumOfLeftLeaves(root)
    print(res)
