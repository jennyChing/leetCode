'''
DP, permutations

62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
from math import factorial
class Solution(object):
    def uniquePaths(self, m, n):
        return factorial(n + m - 2) // factorial(n - 1) // factorial(m - 1)
if __name__ == '__main__':
    res = Solution().uniquePaths(3, 2)
    print(res)


