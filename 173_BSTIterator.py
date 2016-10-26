'''
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
'''
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # inorder tree traversal (left > root > right)
        self._inorder_stack = []
# use the function to first init _inorder_stack with the left subtree down to most left element (= the first smallest element)
        self._inorder_traverse(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._inorder_stack

    def next(self):
        """
        :rtype: int
        """
        cand = self._inorder_stack.pop()
        self._inorder_traverse(cand.right)
        return cand.val

    def _inorder_traverse(self, root):
        while root:
            self._inorder_stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    root.right.right = TreeNode(5)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v += i.next(),
