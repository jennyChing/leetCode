'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
'''


class Solution(object):
    def numTrees(self, n, bst = {}):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        if n in bst:
            return bst[n]
        result = 0
        for i in range(n):
            result += self.numTrees(i, bst) * self.numTrees(n - i - 1, bst)
        bst[n] = result
        return result
