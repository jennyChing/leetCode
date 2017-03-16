'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced_iterative(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        stack, node, last, depths = [], root, None, {}
        print(node.val, stack, last, depths)
        while stack or node:
            if node:
                print(node.val, stack, last, depths)
                stack.append(node)
                node = node.left # reach to most left  leaf
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop() # most recent visited node
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0) # if child node not in the dict, return 0
                    if abs(left - right) > 1:
                        return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True

    def isBalanced_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # idea: need check each root to see if the diff of subtrees' depth is less than 1
        def getDepth(root):
            if not root:
                return 0
            right_dep = getDepth(root.right)
            left_dep = getDepth(root.left)
            if right_dep < 0 or left_dep < 0 or abs(left_dep - right_dep) > 1: # main check
                return -1
            return 1 + max(left_dep, right_dep) # both not -1 so take the max depth as current root's depth

        return getDepth(root) >= 0

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    res = Solution().isBalanced_iterative(root)
    print(res)
