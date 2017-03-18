'''
124. Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
# idea: keep a global max and traverse all paths to compare sum with max
        self.maxSum = -(1<<31)
        def dfs(root):
            if not root:
                return 0
            print(root.val, self.maxSum)
            pathSum = root.val
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            print(root.val, leftmax, rightmax)
            if leftmax > 0:
                pathSum += leftmax
            if rightmax > 0:
                pathSum += rightmax
            self.maxSum = max(self.maxSum, pathSum)
            return max(root.val, root.val + leftmax, root.val + rightmax)
        dfs(root)
        return self.maxSum

if __name__ == '__main__':
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.left.left = TreeNode(-3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    res = Solution().maxPathSum(root)
    print(res)


