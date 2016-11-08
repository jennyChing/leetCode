'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def check(i, j, n, m):
# make the same islands all to 0 to avoid double counting
            if i < 0 or i >= m or j < 0 or j >= n or grid_list[i][j] == '0':
                return
            grid_list[i][j] = '0'
            check(i-1,j,n,m)
            # check(i-1,j+1,n,m,grid_list)
            check(i,j+1,n,m)
            # check(i+1,j+1,n,m,grid_list)
            check(i+1,j,n,m)
            # check(i+1,j-1,n,m,grid_list)
            check(i,j-1,n,m)
            # check(i-1,j-1,n,m,grid_list)

        if grid == []:
            return 0
        m, n = len(grid), len(grid[0])
# string cannot modify in-place for Python so convert grid to nested lists
        grid_list = []
        for i in range(m):
            grid_list.append([])
            for j in range(n):
                grid_list[i].append(grid[i][j])
        if m == 0 and n == 0:
            return 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid_list[i][j] == '1':
                    cnt += 1
                    check(i, j, n, m)
        return cnt

if __name__ == '__main__':
    grid = ["11110","11010","11000","00000"]
    res = Solution().numIslands(grid)
    print(res)

