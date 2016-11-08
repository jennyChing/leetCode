'''
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def __directed_dfs(root, target_sum, path):
            if root == None: # could be negative!
                return
            print(path, target_sum)
            if not root.left and not root.right and target_sum == root.val:
            # when reach leaf, append leaf as the last element in the valid path
                path.append(root.val)
                res.append(path)
            # identify None nodes in the recursive function
            __directed_dfs(root.left, target_sum - root.val, path + [root.val])
            __directed_dfs(root.right, target_sum - root.val, path + [root.val])
        __directed_dfs(root, sum, [])
        return res

if __name__ == "__main__":
    t1 = TreeNode(5)
    t1.left = TreeNode(4)
    t1.right = TreeNode(8)
    t1.left.left = TreeNode(11)
    t1.left.left.left = TreeNode(7)
    t1.left.left.right = TreeNode(2)
    t1.right.left = TreeNode(13)
    t1.right.right = TreeNode(4)
    t1.right.right.right = TreeNode(1)
    t1.right.right.left = TreeNode(5)
    res = Solution().pathSum(t1, 22)
    print(res)
    assert Solution().pathSum(t1, 22) == [[5,4,11,2], [5,8,4,5]]

