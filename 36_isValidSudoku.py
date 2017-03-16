class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        1. check each row and column no repeated 1-9
        2. check within 3x3 space no repeated 1-9
        seperate a function uesd to check if all numbers doesn't repeat using a set (if len(set) < len(nums) then there's dupliate)
        """
        def _isValid(region):
            region = filter(lambda x: x != ".", region)
            return len(set(region)) == len(region)

        for i in range(9):
            if _isValid([board[i][j] for j in range(9)]) == False or _isValid([board[j][i] for j in range(9)]) == False:
                return False

        for i in range(3):
            for j in range(3):
                if _isValid([board[a][b] for a in range(3 * i, 3 * i + 3) for b in range(3 * j, 3 * j + 3)]) == False:
                    return False
        return True


 # Second attempt: hashtable to reduce to O(mn)
        memo_i = {i: set() for i in range(9)}
        memo_s = {(i, j): set() for i in range(3) for j in range(3)}
        for i in range(9):
            memo_j = set()
            for j in range(9):
                if board[i][j] != '.' :
                    if (board[i][j] in memo_j) or (board[i][j] in memo_i[j]) or (board[i][j] in memo_s[(i//3, j//3)]):
                        return False
                    memo_i[j].add(board[i][j])
                    memo_j.add(board[i][j])
                    memo_s[(i//3, j//3)].add(board[i][j])
        return True

if __name__ == '__main__':
    board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    res = Solution().isValidSudoku(board)
    print(res)
