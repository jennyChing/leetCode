'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        i, j, width = len(matrix) - 1, 0, len(matrix[0])
        print(i, j, matrix[i][j], target)
        while i >= 0 and j < width:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i -= 1
                print("less then target :", i, j, matrix[i][j], target)
            else:
                j += 1
                print("more then target :", i, j, matrix[i][j], target)
        return False
if __name__ == '__main__':
    matrix =[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    matrix = [[-1], [-1]]
    target = 2
    res = Solution().searchMatrix(matrix, target)
    print(res)
