'''
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val > key: # traverse left sub tree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # traverse right sub tree
            root.right = self.deleteNode(root.right, key)
        else: # check base case
            if not root.left: # one right child or no child
                return root.right
            if not root.right: # one left child
                return root.left
            if root.left and root.right: # 2 children
                leftSubtree = root.left
                while leftSubtree.right:
                    leftSubtree = leftSubtree.right
                root.val = leftSubtree.val
                root.left = self.deleteNode(root.left, root.val)
        return root


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    key = 3
    res = Solution().deleteNode(root, key)
    while res:
        print(res.val)
        res = res.left

