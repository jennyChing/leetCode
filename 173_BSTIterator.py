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
        self._data = []
        self._push_all(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return relf._data

    def next(self):
        """
        :rtype: int
        """
        cand = self._data.pop()
        self._push_all(cand.right)
        return cand.val

    def _push_all(self, root):
        while root:
            print(self._data)
            self._data += root,
            root = root.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v += i.next()
        print(v)
