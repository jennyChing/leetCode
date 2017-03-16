'''
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
'''
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = [[1,-1], [-1,1]]
        dirt_idx = i = j = 0
        res = []
        n, m = len(matrix), len(matrix[0])
        while len(res) < n * m:
            res.append(matrix[i][j])
            next_i, next_j = i + direction[dirt_idx][1], j + direction[dirt_idx][0]
            if next_i >= n:
                j += 1
                dirt_idx = (dirt_idx + 1) % 2
            elif next_j < 0:
                dirt_idx = (dirt_idx + 1) % 2
                i += 1
            elif next_j >= m:
                dirt_idx = (dirt_idx + 1) % 2
                i += 1
            elif next_i < 0:
                dirt_idx = (dirt_idx + 1) % 2
                j += 1
            else:
                i, j = i + direction[dirt_idx][1], j + direction[dirt_idx][0]
        return res

if __name__ == '__main__':
    matrix = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    res = Solution().findDiagonalOrder(matrix)
    print(res)

