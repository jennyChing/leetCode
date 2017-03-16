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
        res = []

        for j in range(n):
            i, filled = 0, 0
            partial, stack = [], []
            memo_topLeft, memo_downRight, memo_row, memo_col = set(), set(), set(), set()

            while i < n and j < n:
                print(i, j, partial, filled)
                if i + j not in memo_downRight and i - j not in memo_topLeft and i not in memo_row and j not in memo_col:
                    filled += 1
                    partial.append((i, j))
                    memo_row.add(i)
                    memo_topLeft.add(i - j)
                    memo_col.add(j)
                    memo_downRight.add(i + j)
                    if filled == n:
                        res.append(partial)
                    else:
                        i += 1 # next row
                        j = 0 # first col
                else:
                    if j + 1 < n:
                        j += 1
                    else:
                        filled -= 1
                        if not stack:
                            print("break")
                            break
                        i, j = stack.pop()
                        memo_row.remove(i)
                        memo_col.remove(j)
        return res

if __name__ == '__main__':
    res = Solution().solveNQueens(5)
    print(res)

