'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSame(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                print(left.val, right.val)
                return False
            return isSame(left.left, right.right) and isSame(right.left, left.right)
        return not root or isSame(root.left, root.right)
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(Solution().isSymmetric(root))
    assert Solution().isSymmetric(root)
