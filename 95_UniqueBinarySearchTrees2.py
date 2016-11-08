'''
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def __directed_generate(start, end):
            trees = []
# for loop iterate to include all combinations:
            for root in range(start, end + 1):
                for left in __directed_generate(start, root - 1):
                    for right in __directed_generate(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]
        return [] if not n else __directed_generate(1, n)

if __name__ == "__main__":
    res = Solution().generateTrees(3)
    for r in res:
        print(r.val)
    t1 = TreeNode(2)
    t1.left = TreeNode(1)
    t1.right = TreeNode(3)
    t2 = TreeNode(3)
    t2.left = TreeNode(2)
    t2.left.left = TreeNode(1)
    t3 = TreeNode(3)
    t3.left = TreeNode(1)
    t3.left.right = TreeNode(2)
    t4 = TreeNode(1)
    t4.right = TreeNode(2)
    t4.right.right = TreeNode(3)
    t5 = TreeNode(1)
    t5.right = TreeNode(3)
    t5.right.left = TreeNode(2)




