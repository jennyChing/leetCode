import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        traverse and print each level's nodes
        print leaves first, then delete the leaves and move up one level to the new leaves
        """
        res, curr_level = [], collections.deque([root])
        while curr_level:
            next_level, curr_level_val = collections.deque([]), []
            while curr_level: # BFS
                node = curr_level.popleft()
                curr_level_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            res.append(curr_level_val)
        return res[::-1]

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.left.right = TreeNode(17)
    res = Solution().levelOrderBottom(root)
    print(res)


