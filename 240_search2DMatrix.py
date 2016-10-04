'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        def searchInsert(self, nums, n):
            left, right = 0, len(nums)
            while right > left:
                mid = (right - left) // 2 + left
                if n == nums[mid]:
                    return mid
                elif n > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            if n < nums[mid]:
                return mid
            return mid + 1
        j, k = 0, 0
        if len(matrix) == 1:
            return True if matrix[0][0] == target else False
        for i in range(min(len(matrix), len(matrix[0]))):
            print([x[i] for x in matrix])
            print(len(matrix), len(matrix[0]))
            j, k = searchInsert(self, [x[i] for x in matrix], target), searchInsert(self, matrix[k], target)
            print(j, k, i)
            if j > len(matrix) or k > len(matrix[0]):
                return False
            if matrix[j][i] == target or matrix[i][k] == target:
                return True
        return False
if __name__ == '__main__':
    matrix =[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    matrix = [[-1], [3]]
    target = 3
    res = Solution().searchMatrix(matrix, target)
    print(res)
