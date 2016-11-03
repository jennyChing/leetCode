'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
# first create a new triangle to record the DP min path
        n = len(triangle)
        DP = [[0] * (i + 1) for i in range(n)]
        DP[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    DP[i][j] = DP[i - 1][j] + triangle[i][j]
                elif j == i:
                    DP[i][j] = DP[i - 1][j - 1] + triangle[i][j]
                else:
                    DP[i][j] = triangle[i][j] + min(DP[i - 1][j - 1], DP[i - 1][j])
        print(DP)
        return min(DP[-1])


if __name__ == '__main__':
    nums = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    res = Solution().minimumTotal(nums)
    print(res)
