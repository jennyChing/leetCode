'''
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BurceForce_Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def __dfs(root, target): # use root as start node to traverse
            if not root:
                return
            print(root.val, target)
            if root.val == target:
                self.cnt[0] += 1
                print(self.cnt)
            __dfs(root.left, target - root.val)
            __dfs(root.right, target - root.val)

        self.cnt = [0]
        if root: # use each node as new start
           # print(__dfs(root.right, sum), __dfs(root, sum))
            __dfs(root, sum)
            self.pathSum(root.left, sum)
            self.pathSum(root.right, sum)
        return self.cnt[0]

import collections
class Two_sum_Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        def __dfs(root, target, so_far, memo):
            if not root:
                return
            print(memo)
            remaining = so_far + root.val - target
            print("node:", root.val, "sum:", target, "so far:", so_far, "what's left:",  remaining)
            if remaining in memo:
                self.cnt += memo[remaining]
                print(memo[remaining])
            memo[so_far + root.val] += 1
            print(root.val)
            print(memo)
            # each node only traverse once, use memo to record remaining
            __dfs(root.right, target, so_far + root.val, memo)
            __dfs(root.left, target, so_far + root.val, memo)
            memo[so_far + root.val] -= 1 # cannot reuse paths (unique)
        memo = collections.defaultdict(int)
        memo[0] = 1
        __dfs(root, sum, 0, memo)
        return self.cnt


if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.right.right = TreeNode(11)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    root.left.right.right = TreeNode(1)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)

    #root = TreeNode(1)
    #root.right = TreeNode(2)
    #root.right.right = TreeNode(3)
    #root.right.right.right = TreeNode(4)
    #root.right.right.right.right = TreeNode(5)

    #root = TreeNode(1)
    #root.left = TreeNode(-2)
    #root.right = TreeNode(-3)
    #root.right.left = TreeNode(-2)
    #root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    #root.left.left.left = TreeNode(-1)

    res = BurceForce_Solution().pathSum(root, 8)
    print(res)
