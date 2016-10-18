'''
DP
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution(object):
    def minPathSum(self, grid):
        '''
        update the num in the matrix when the left & up neighbor is updated
        '''
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]
        for j in range(1, len(grid)):
            grid[j][0] += grid[j - 1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            print(grid)
        return grid[-1][-1]
if __name__ == '__main__':
    matrix = [[10, 2, 3, 11], [1, 6, 5, 7], [8, 2, 5, 12]]
    res = Solution().minPathSum(matrix)
    print(res)

