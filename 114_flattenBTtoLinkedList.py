'''
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
# [idea] starting from root, insert my left subtree between root and my right subtree, and go down to most right of my left subtree and link my original right subtree under it => O(n)

        while root: # not root.right
            original_right = root.right
            root.right = root.left
            root.left = None
# use a copy to move down to most right instead of moving root.right
            copy = root
            while copy.right:
                copy = copy.right
            copy.right = original_right
            root = root.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    Solution().flatten(root)


