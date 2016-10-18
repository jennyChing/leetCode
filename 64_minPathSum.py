'''
DP
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution(object):
    def minPathSum(self, grid):
        dist = [float('inf')] * len(grid) * len(grid[0])
        print(dist)
if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    res = Solution().minPathSum(matrix)
