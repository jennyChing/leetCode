'''
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: loop with BFS to find the right path (all use .right value)
        """
        if root == None:
            return []
        currLevel, nextLevel = deque([root]), deque([])
        rv = []
        lev = 0
        while currLevel:
            lev += 1
            rv.append(currLevel[0].val)
            while currLevel:
                node = currLevel.popleft()
                print(lev, node.val)
                if node.right:
                    nextLevel.append(node.right)
                if node.left:
                    nextLevel.append(node.left)
            currLevel, nextLevel = nextLevel, deque([])
        return rv
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(4)
    res = Solution().rightSideView(root)
    print(res)


