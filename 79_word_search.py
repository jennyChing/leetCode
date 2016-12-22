'''
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        Backtracking base case:
        """
        if not word:
            return True
        if not board:
            return False

        def __directed_dfs(i, j, word, visited):
            # Check word[0] first!!
            if board[i][j] == word[0] and (i, j) not in visited:
                # base case return
                if not word[1:]:
                    return True
                # backtracking: use a stack to record nodes visited and pop when reach invalid path
                visited.add((i, j))
                if i > 0 and __directed_dfs(i - 1, j, word[1:], visited):
                    return True
                if i < len(board) - 1 and __directed_dfs(i + 1, j, word[1:], visited):
                    return True
                if j > 0 and __directed_dfs(i, j - 1, word[1:], visited):
                    return True
                if j < len(board[0]) - 1 and  __directed_dfs(i, j + 1, word[1:], visited):
                    return True
                # renew the set to not using i, j
                visited.remove((i, j))
                return False
            else:
                return False

        visited = set()
        # find all the valid starting point and recursive from there
        for i in range(len(board)):
            for j in range(len(board[0])):
                if __directed_dfs(i, j, word, visited):
                        return True
        return False


if __name__ == "__main__":
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    word = "SEE"
    res = Solution().exist(board, word)
    print(res)
