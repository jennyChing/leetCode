'''
515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # idea: bfs level traversal and append the max value for each row
        curLevel = collections.deque([root])
        res = []
        while curLevel:
            nextLevel = collections.deque()
            curVal = []
            while curLevel:
                node = curLevel.popleft()
                curVal.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(max(curVal))
            curLevel = nextLevel
        return res

if __name__ == '__main__':
    root = TreeNode(
    res = Solution().largestValues(root)

