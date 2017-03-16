'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class shortSolution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root_idx = preorder[0]


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        node_to_index = {}
        for i, v in enumerate(inorder):
            node_to_index[v] = i

        def __directed_build(p_start, p_end, i_start, i_end):
            if p_start >= p_end:
                return
            left_size = node_to_index[preorder[p_start]] - i_start
            print(left_size)
            root = TreeNode(preorder[p_start])
            root.left = __directed_build(p_start + 1, p_start + 1 + left_size, i_start, node_to_index[preorder[p_start]])
            root.right = __directed_build(p_start + 1 + left_size, p_end, node_to_index[preorder[p_start]] + 1, i_end)
            return root
        return __directed_build(0, len(preorder), 0, len(inorder))


if __name__ == "__main__":
    res = Solution().buildTree([1,2], [1,2])
    while res:
        print(res.val)
        if not res.left and not res.right:
            break
        if res.left:
            res = res.left
        if res.right:
            res = res.right
