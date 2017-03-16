'''
105. Construct Binary Tree from postorder and Inorder Traversal

Given postorder and inorder traversal of a tree, construct the binary tree.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type postorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def __directed_build(p_start, p_end, i_start, i_end):
            if p_start >= p_end:
                return
            root = TreeNode(postorder[p_end - 1])
            root_idx = node_to_index[postorder[p_end - 1]]

        # Calculate size of nodes for each side:
            left_size = root_idx - i_start

            root.left = __directed_build(p_start, p_start + left_size, i_start, root_idx)
            root.right = __directed_build(p_start + left_size, p_end - 1, root_idx + 1, i_end)
            return root

        node_to_index = {}
        for i, v in enumerate(inorder):
            node_to_index[v] = i
        return __directed_build(0, len(postorder), 0, len(inorder))


if __name__ == "__main__":
    res = Solution().buildTree([1,2,3], [3,2,1])
    res = Solution().buildTree([2,1], [2,1])
    while res:
        print(res.val)
        if not res.left and not res.right:
            break
        if res.left:
            res = res.left
        if res.right:
            res = res.right
