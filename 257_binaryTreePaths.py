# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return []
        elif root.right == None and root.left == None:
            return [str(root.val)]
        res = []
        for p in self.binaryTreePaths(root.left):
            res.append(str(root.val) + '->' + p)
        for p in self.binaryTreePaths(root.right):
            res.append(str(root.val) + '->' + p)
        return res
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    res = Solution().binaryTreePaths(root)
    print(res)



