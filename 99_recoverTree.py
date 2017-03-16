'''
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
# idea: use dfs to check whether root.val is between left and right subtree
        if not root:
            return
        if root.left and root.right and root.left.val < root.val < root.right.val: # no need to swap nodes
            self.recoverTree(root.left)
            self.recoverTree(root.right)
        # swap with most right in left subtree
        if root.left and root.val < root.left.val:
            leftSub = root.left
            while leftSub.right:
                leftSub = leftSub.right
            root.val, leftSub.val = leftSub.val, root.val
            self.recoverTree(root.left)

        # swap with most right in left subtree
        if root.right and root.val > root.right.val:
            rightSub = root.right
            while rightSub.left:
                rightSub = rightSub.left
            root.val, rightSub.val = rightSub.val, root.val
            self.recoverTree(root.right)

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    res = Solution().recoverTree(root)
    while res:
        print(res.val)
        res = res.left

