'''
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def __cnt_side(i, j):
            sides = 0
            if i > 0:
                if grid[i - 1][j] == 1:
                    sides += 1
            if i + 1 < n:
                if grid[i + 1][j] == 1:
                    sides += 1
            if j > 0:
                if grid[i][j - 1] == 1:
                    sides += 1
            if j + 1 < m:
                if grid[i][j + 1] == 1:
                    sides += 1
            return 4 - sides

        n, m = len(grid), len(grid[0])
        perimeter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    perimeter += __cnt_side(i, j)
        return perimeter


if __name__ == "__main__":
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    res = Solution().islandPerimeter(grid)
    print(res)
