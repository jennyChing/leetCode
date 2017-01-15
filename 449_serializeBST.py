'''
449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def __traverse(root, res):
            res.append(str(root.val))
            if root.left:
                res = __traverse(root.left, res)
            if root.right:
                res = __traverse(root.right, res)
            return res
        return ','.join(__traverse(root, []))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def __traverse(idx, root):
            if root.val < nodes[idx]: # right subtree
                root.right = __traverse(idx + 1, root.right)


        nodes = data.split(",")
        if nodes[0] == '': return None
        root = TreeNode(int(nodes[0]))
        curr = root
        upperBound = float('inf')
        nodes = nodes[1:]
        # upperBound = sys.maxint
        for n in nodes:
            n = int(n)
            if n < prev.val: # node belong to root's left subtree
                prev.left = TreeNode(n)
                upperBound = prev.val
            # the node before left subtree is current root, so record as prev
                stack.append(prev) # first record current root then move left
                prev = prev.left
            elif n < upperBound: # node belong to root's right subtree
                prev.right = TreeNode(n)
                prev = prev.right
            else: #
                while len(stack) > 0 and n > stack[-1].val: # right
                    print([s.val for s in stack], n)
                    prev = stack.pop()
                prev.right = TreeNode(n)
                prev = prev.right
                if len(stack) > 0:
                    upperBound = stack[-1].val
                else:
                    upperBound = float('inf')
                    #upperBound = sys.maxint
        return root

# Your Codec object will be instantiated and called as such:
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(21)
    codec = Codec()
    data = (codec.serialize(root))
    codec.deserialize(data)
