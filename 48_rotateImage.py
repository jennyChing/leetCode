'''
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

# Easy: create a new list
        res = []
        for i in range(n - 1, -1, -1):
            res.append([])
            print(res)
            for j in range(n - 1, -1, -1):
                 res[n - i - 1].append(matrix[j][n - 1- i])
                 print(res)
# Hard: do it in-place
        print(matrix)
# step1: convert based on line x=y
        for i in range(n):
            for j in range(i, n):
                print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

# step2: convert left to right
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix


if __name__ == "__main__":
    res = Solution().rotate([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    print(res)


