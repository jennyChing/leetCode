'''
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __directed_depth(self, root):
        if not root:
            return 0
        return 1 + self.__directed_depth(root.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_dep = self.__directed_depth(root.left)
        right_dep = self.__directed_depth(root.right)
        print("root", root.val, "left/right:", left_dep, right_dep)
        if left_dep == right_dep:
            print(pow(2, left_dep))
            return pow(2, left_dep) + self.countNodes(root.right)
        else:
            print(pow(2, right_dep))
            return pow(2, right_dep) + self.countNodes(root.left)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.right.left.left = TreeNode(12)
    res = Solution().countNodes(root)
    print(res)
