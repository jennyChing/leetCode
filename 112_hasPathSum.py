# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        keep a list of frontier nodes in a stack, and a traversed tree
        use DFS to check each path in a tree: return when both left and right child are leaves
        """
        if not root:
            return False
        if not root.right and not root.left: # when both child is leaves
            return sum == root.val
        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val) # minus the current root value from sum and move to the child nodes

if __name__ == "__main__":
    t1 = TreeNode(5)
    t1.left = TreeNode(4)
    t1.right = TreeNode(8)
    t1.left.left = TreeNode(11)
    t1.left.left.left = TreeNode(7)
    t1.left.left.right = TreeNode(2)
    t1.right.left = TreeNode(13)
    t1.right.right = TreeNode(4)
    t1.right.right.right = TreeNode(1)
    assert Solution().hasPathSum(t1, 22) == True
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    assert Solution().hasPathSum(t1, 1) == False
