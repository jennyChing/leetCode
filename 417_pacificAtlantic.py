'''
417. Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix == []:
            return []
        def __directed_dfs_p(i, j):
            if memo_p[i][j] == False:
                return
            if i + 1 < n and memo_p[i + 1][j] == False and matrix[i][j] <= matrix[i + 1][j]:
                memo_p[i + 1][j] = True
                __directed_dfs_p(i + 1, j)
            if j + 1 < m and memo_p[i][j + 1] == False and matrix[i][j] <= matrix[i][j + 1]:
                memo_p[i][j + 1] = True
                __directed_dfs_p(i, j + 1)
            if i > 0 and memo_p[i - 1][j] == False and matrix[i][j] <= matrix[i - 1][j]:
                memo_p[i - 1][j] = True
                __directed_dfs_p(i - 1, j)
            if j > 0 and memo_p[i][j - 1] == False and matrix[i][j] <= matrix[i][j - 1]:
                memo_p[i][j - 1] = True
                __directed_dfs_p(i, j - 1)

        def __directed_dfs_a(i, j):
            if memo_a[i][j] == False:
                return
            if i + 1 < n and memo_a[i + 1][j] == False and matrix[i][j] <= matrix[i + 1][j]:
                memo_a[i + 1][j] = True
                __directed_dfs_a(i + 1, j)
            if j + 1 < m and memo_a[i][j + 1] == False and matrix[i][j] <= matrix[i][j + 1]:
                memo_a[i][j + 1] = True
                __directed_dfs_a(i, j + 1)
            if i > 0 and memo_a[i - 1][j] == False and matrix[i][j] <= matrix[i - 1][j]:
                memo_a[i - 1][j] = True
                __directed_dfs_a(i - 1, j)
            if j > 0 and memo_a[i][j - 1] == False and matrix[i][j] <= matrix[i][j - 1]:
                memo_a[i][j - 1] = True
                __directed_dfs_a(i, j - 1)

        n, m = len(matrix), len(matrix[0])
        memo_p, memo_a = [[False] * m for _ in range(n)], [[False] * m for _ in range(n)]

# start dfs from 4 sides of the matrix
        for i in range(n):
            memo_p[i][0] = True
            __directed_dfs_p(i, 0)
        for j in range(m):
            memo_p[0][j] = True
            __directed_dfs_p(0, j)
        for i in range(n - 1, -1, -1):
            memo_a[i][m - 1] = True
            __directed_dfs_a(i, m - 1)
        for j in range(m - 1, -1, -1):
            memo_a[n - 1][j] = True
            __directed_dfs_a(n - 1, j)

        res = []
        for i in range(n):
            for j in range(m):
                if memo_a[i][j] == True and memo_p[i][j] == True:
                    res.append([i, j])
        return res


if __name__ == "__main__":
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    res = Solution().pacificAtlantic(matrix)
    print(res)
