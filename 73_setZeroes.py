'''
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        i_arr, j_arr = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_arr.append(i)
                    j_arr.append(j)
        print(i_arr, j_arr)
        for i in i_arr:
            matrix[i] = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in j_arr:
                matrix[i][j] = 0
        return matrix

if __name__ == '__main__':
    matrix = [[1,2,3],[3,0,2],[5,3,0]]
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    res = Solution().setZeroes(matrix)
    print(res)

