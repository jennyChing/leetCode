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
        pathSum = 0
        stack, path = [root], []
        def __directed_dfs(root, path, stack, pathSum):
            if not root.left and not root.right:
                pathSum += sum(path)
                print(pathSum, path)
            while stack:
                path.append(stack.pop().val)
                if root.left:
                    stack.append(root.left)
                    __directed_dfs(root.left, path, stack, pathSum)
                if root.right:
                    stack.append(root.right)
                    __directed_dfs(root.right, path, stack, pathSum)
        __directed_dfs(root, path, stack, pathSum)
        return pathSum


if __name__ =='__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = Solution().sumNumbers(root)
    print(res)


