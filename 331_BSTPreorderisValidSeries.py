'''
331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
'''
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        print(nodes)
        self.index = -1

        def preorder_traverse():
            self.index += 1
            print(nodes[self.index])
            if nodes[self.index] == '#':
            # only return when end of this subtree
                return None
            left = preorder_traverse()
            print("left of ", self.index, nodes[self.index], left)
            right = preorder_traverse()
            print("right of ", self.index, nodes[self.index], right)
        # return True if both right and left subtree is None
            assert (not left and not right)
        try:
        # check the nodes traversed count and the nodes in the list
            preorder_traverse()
            return self.index == len(nodes) - 1
        except:
            return False
if __name__ == '__main__':
    res = Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(res)



