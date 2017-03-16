'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
import collections
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(v, i, j, i_dict, j_dict, sq_dict, visited):
            print(i_dict[i], visited)
            if board[i][j] != '.' or (i, j) in visited:
                return
            if (board[i][j] in i_dict[i]) or (board[i][j] in j_dict[j]) or (board[i][j] in sq_dict[(i // 3, j // 3)]):
                return
            board[i][j] = v
            visited.add((i, j))
            for n in "123456789":
                if i + 1 < 9: # move down
                    i_dict[i].add(n)
                    j_dict[j].add(n)
                    print("added:", i_dict[i + 1])
                    sq_dict[((i + 1) // 3, j // 3)].add(n)
                    dfs(n, i + 1, j, i_dict, j_dict, sq_dict, visited)
                    print("remove now:", i_dict[i + 1])
                    #i_dict[i + 1].remove(n) # resest
                    j_dict[j].remove(n)
                    sq_dict[((i + 1) // 3, j // 3)].remove(n)
                if j + 1 < 9: # move right
                    i_dict[i].add(n)
                    j_dict[j + 1].add(n)
                    sq_dict[(i // 3, (j + 1) // 3)].add(n)
                    dfs(n, i, j + 1, i_dict, j_dict, sq_dict, visited)
                    i_dict[i].remove(n)
                    j_dict[j + 1].remove(n) # resest
                    sq_dict[(i // 3, (j + 1) // 3)].remove(n)
                if i - 1 >= 0: # move up
                    i_dict[i - 1].add(n)
                    j_dict[j].add(n)
                    sq_dict[((i - 1) // 3, j // 3)].add(n)
                    dfs(n, i - 1, j, i_dict, j_dict, sq_dict, visited)
                    i_dict[i - 1].remove(n) # resest
                    j_dict[j].remove(n)
                    sq_dict[((i - 1) // 3, j // 3)].remove(n)
                if j - 1 >= 0: # move left
                    i_dict[i].add(n)
                    j_dict[j - 1].add(n)
                    sq_dict[(i // 3, (j - 1) // 3)].add(n)
                    dfs(n, i, j - 1, i_dict, j_dict, sq_dict, visited)
                    i_dict[i].remove(n)
                    j_dict[j - 1].remove(n) # resest
                    sq_dict[(i // 3, (j - 1) // 3)].remove(n)

        # first take all existing cells into pre-populated dicts
        i_dict = {i: set() for i in range(9)}
        j_dict = {i: set() for i in range(9)}
        sq_dict = {(i, j): set() for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    i_dict[i].add(board[i][j])
                    j_dict[j].add(board[i][j])
                    sq_dict[(i // 3, j // 3)].add(board[i][j])

        dfs(1, 0, 0, i_dict, j_dict, sq_dict, set())


if __name__ == '__main__':
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    res = Solution().solveSudoku(board)
    print(res)
