# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # count nodes below given node
        def countNodes(root):
            if not root:
                return 0
            l = countNodes(root.left)
            r = countNodes(root.right)
            return l + r + 1
        def getkth(root, k):
            # first count all nodes smaller then root (all nodes if left subtree)
            cnt = countNodes(root.left)
            # case 1: the root is exactly kth element
            if cnt + 1 == k:
                return root.val
            # case 2: the nodes smaller then root is less then k, meaning kth is on the right subtree of root
            elif cnt + 1 < k:
                return getkth(root.right, k - 1 - cnt) # known that at least cnt + 1 elements are smaller then root
            else:
                return getkth(root.left, k)
            # case 3: the nodes smaller then root is more then k, meaning kth is on the left subtree of root
        return getkth(root, k)

if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right = TreeNode(10)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(14)
    res = Solution().kthSmallest(root, 3)
    print(res)
    assert res == 6
