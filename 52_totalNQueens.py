'''
52. N-Queens II
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
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
        return len(res)

if __name__ == '__main__':
    res = Solution().solveNQueens(5)
    print(res)

