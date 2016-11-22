'''
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    # use bfs to traverse one level at a time
        def bfs(flag, root, trav):
            currlevel = [root]
            while currlevel:
                nextlevel = []
                temp = []
                for node in currlevel: # currlevel is a queue
                    temp.append(node.val)
                    if node.left: nextlevel.append(node.left)
                    if node.right: nextlevel.append(node.right)
                currlevel = nextlevel # move down to next level
                trav.append(temp[::flag])
                flag *= -1 # use a flag to record direction

        trav = []
        bfs(1, root, trav)
        return trav

if __name__ == "__main__":
    t1 = TreeNode(3)
    t1.left = TreeNode(9)
    t1.right = TreeNode(20)
    t1.right.left = TreeNode(15)
    t1.right.right = TreeNode(7)
    res = Solution().zigzagLevelOrder(t1)
    print(res)



