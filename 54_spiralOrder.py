'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(matrix), len(matrix[0])
        res = []
        visited = set()
        drct = [[0, 1], [1, 0], [0, -1], [-1, 0]] #right, down, left, up
        i, j, d_idx = 0, 0, 0 # start from going right
        while len(res) < m * n:
            res.append(matrix[i][j])
            if i + drct[d_idx][0] < 0 or i + drct[d_idx][0] >= n or j + drct[d_idx][1] < 0 or j + drct[d_idx][1] >= m or (i + drct[d_idx][0], j + drct[d_idx][1]) in visited:
                d_idx = (d_idx + 1) % 4
            visited.add((i, j))
            i += drct[d_idx][0]
            j += drct[d_idx][1]
        return res
if __name__ == "__main__":
    matrix = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
    res = Solution().spiralOrder(matrix)
    print(res)
