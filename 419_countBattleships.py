'''
419. Battleships in a Board

Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
'''
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    cnt += 1
                    tmp_i, tmp_j = i + 1, j + 1
                    while tmp_j < m and board[i][tmp_j] == 'X':
                        board[i][tmp_j] = '.'
                        tmp_j += 1
                    while tmp_i < n and board[tmp_i][j] == 'X':
                        board[tmp_i][j] = '.'
                        tmp_i += 1
        return cnt

    def countBattleships_refer(self, board): # one pass and no modify
        cnt = 0
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'): # check not duplicate count
                    cnt += 1
        return cnt

if __name__ == "__main__":
    board = [["X", "X",".", "X"],[".", ".", ".", "X"],[".", ".", ".", "X"]]
    board = [["X", "X", "X"] ]
    res = Solution().countBattleships_refer(board)
    print(res)
