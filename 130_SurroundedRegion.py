'''
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
import collections
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        def __check_around(i, j):
            q = collections.deque([(i, j)])
            while q:
                i, j = q.popleft()
                if 0 <= i < n and 0 <= j < m and board[i][j] == 'O': # delay the check
                    board[i][j] = "@"
                    q.append([i - 1, j])
                    q.append([i + 1, j])
                    q.append([i, j - 1])
                    q.append([i, j + 1])

        # Step1: start from all O groups that are on side and mark them as @
        for i in range(n):
            j = 0
            __check_around(i, j)
            j = m - 1
            __check_around(i, j)

        for j in range(m):
            i = 0
            __check_around(i, j)
            i = n - 1
            __check_around(i, j)
        # Step2: for the rest that are still Os, flip them into Xs and turn @ back to Os
        for i in range(n):
            for j in range(m):
                board[i][j] = "O" if board[i][j] == "@"  else "X"

if __name__ == "__main__":
    board = [["X", "X", "X", "X"],["O","O","X","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    Solution().solve(board)
    print(board)
