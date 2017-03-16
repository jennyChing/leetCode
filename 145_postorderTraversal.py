'''
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # postorder: left -> right -> root
        if not root:
            return
        res = []
        res += self.postorderTraversal(root.left) if root.left else []
        res += self.postorderTraversal(root.right) if root.right else []
        res.append(root.val)
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    res = Solution().postorderTraversal(root)
    print(res)

