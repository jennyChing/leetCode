'''
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root: None} # key: node, value: node's parent
        stack = [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

    # when meet both q and p, start moving up the check LCA
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p] # move up to p's parent
        while q not in ancestors:
            q = parent[q] # move up to q's parent
        return q

if __name__ == "__main__":
    t1 = TreeNode(3)
    t1.left = TreeNode(5)
    t1.right = TreeNode(1)
    t1.left.left = TreeNode(6)
    t1.left.right = TreeNode(2)
    t1.left.right.right = TreeNode(4)
    t1.left.right.left = TreeNode(7)
    t1.right.left = TreeNode(0)
    t1.right.right = TreeNode(8)
    res = Solution().lowestCommonAncestor(t1, t1.left, t1.left.right.right)


