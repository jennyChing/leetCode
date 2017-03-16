'''
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def __directed_dfs(root, pathSum):
            if not root:
                return 0
            pathSum = 10 * pathSum + root.val
            if not root.left and not root.right: # reach leaf
                return pathSum
            return __directed_dfs(root.left, pathSum) + __directed_dfs(root.right, pathSum)
        return __directed_dfs(root, 0)

if __name__ =='__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    res = Solution().sumNumbers(root)
    print(res)


