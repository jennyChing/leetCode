'''
289. Game of Life

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state.

'''
class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board[0]), len(board)

        # Helper function to calculate the lives around i, j:
        def check(i, j, board):
            cnt = 0
            # Check if initial status is dead or live: % 2
            if i - 1 >= 0: cnt += board[i - 1][j] % 2
            if j - 1 >= 0: cnt += board[i][j - 1] % 2
            if i - 1 >= 0 and j - 1 >= 0: cnt += board[i - 1][j - 1] % 2
            if i + 1 < n: cnt += board[i + 1][j] % 2
            if j + 1 < m: cnt += board[i][j + 1] % 2
            if i + 1 < n and j + 1 < m: cnt += board[i + 1][j + 1] % 2
            if i + 1 < n and j - 1 >= 0: cnt += board[i + 1][j - 1] % 2
            if j + 1 < m and i - 1 >= 0: cnt += board[i - 1][j + 1] % 2
            return cnt

        # Do in-place modification:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 or board[i][j] == 2: # dead or dead2live
                    # if the cell has 3 lives around it, mark as 2:
                    if check(i, j, board) == 3: board[i][j] = 2
                else:
                    # if less then 2 or over 3 lives around it, mark as 3:
                    if check(i, j, board) > 3 or check(i, j, board) < 2:
                        board[i][j] = 3

        for i in range(n):
            for j in range(m):
                if board[i][j] == 2: board[i][j] = 1
                elif board[i][j] == 3: board[i][j] = 0

if __name__ == '__main__':
    board = [[0, 0, 1],[1, 0, 1],[1, 0, 0]]
    Solution().gameOfLife(board)
    print(board)


