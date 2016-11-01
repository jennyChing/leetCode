'''
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
# DP and obstacleGrid will be off by one coz 補上 left and up row to handle corner case
        print(DP)
        DP[0][1] = 1 # initialize
        print(DP)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not obstacleGrid[i - 1][j - 1]: # curr cell not obstacle
                    DP[i][j] = DP[i][j - 1] + DP[i - 1][j]
                    print(DP)
        return DP[n][m]
if __name__ == '__main__':
    nums = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    nums = [[0]]
    res = Solution().uniquePathsWithObstacles(nums)
    print(res)



