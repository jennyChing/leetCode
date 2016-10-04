'''
337. House Robber III

DFS (binary tree)

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
# easy version: rob all the money
        #def DFS(root):
        #    if not root:
        #        return 0
        #    if root in self.memo:
        #        return self.memo[root]
        #    money = root.val
        #    money += DFS(root.left) + DFS(root.right)
        #    self.memo[root] = money
        #    return money
        #return DFS(root)
# advanced version: rob separate level houses
        def DFS(root):
            if not root:
                return 0
            if root in self.memo:
                return self.memo[root]
            else:
                self.memo[root] = 0
            # case1: rob this house and the next next level ones
            rob_this = root.val
            rob_this += DFS(root.left.left) + DFS(root.left.right) if root.left else 0
            rob_this += DFS(root.right.left) + DFS(root.right.right) if root.right else 0
            print(rob_this)
            # case2: not rob this house but the next level ones
            rob_next = DFS(root.left) + DFS(root.right)
            print(rob_next)
            # important step: record the node money value into the dictionary "memo"
            self.memo[root] = max(self.memo[root], max(rob_this, rob_next))
            return self.memo[root]
        return DFS(root)
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(2)
    res = Solution().rob(root)
    print(res)


