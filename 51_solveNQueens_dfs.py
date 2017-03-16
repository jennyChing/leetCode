'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]]
'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
# key: use stack to record placed queens, pop the stack when run out of room in a row and move back to previous row
        def valid_col(cols, n):
            for i in range(n):
                if abs(cols[i] - cols[n]) == n - i or cols[i] == cols[n]:
                    return False
            return True

        def dfs(row, cols, partial):
            if row == n:
                res.append(partial)
                return # backtrack
            for i in range(n): # each row generate dfs to check if valid
                cols[row] = i # this row fill at ith column
                if valid_col(cols, row):
                    tmp = "." * len(cols)
                    dfs(row + 1, cols, partial + [tmp[:i] + "Q" + tmp[i + 1:]])

        res = []
        dfs(0, [-1] * n, [])
        return res

if __name__ == '__main__':
    res = Solution().solveNQueens(5)
    print(res)

