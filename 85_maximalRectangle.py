'''
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
# idea: iterate each row as ground to find the max rec
        if not matrix or not matrix[0]: return 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * (m + 1)
        rec = 0
        for row in matrix: # treat each row xas ground to find max rec
            for i in range(m):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i, v in enumerate(heights):
                while v < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    rec = max(rec, h * w)
                stack.append(i)
        return rec

if __name__ == '__main__':
    matrix = ["10100","10111","11111","10010"]
    res = Solution().maximalRectangle(matrix)
    print(res)

