'''
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [[True, []]] + [[False, []] for _ in range(len(s))] # idx 0: empty string
        for i in range(1, len(s) + 1): # s index is off by one with dp array
            for w in wordDict:
                #if s[i - 1:i - 1 + len(w)] == w and dp[i - 1]:
                if s[i - 1:].startswith(w) and dp[i - 1][0]:
                    dp[i - 1 + len(w)][0] = True
                    dp[i - 1 + len(w)][1].append(w)
        res = []
        def dfs(path, i):
            if i == 0:
                res.append(path)
            for w in dp[i][1]:
                dfs([s[i - len(w):i]] + path, i - len(w))

        dfs([], len(s))
        return [" ".join(r) for r in res]

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    res = Solution().wordBreak(s, wordDict)
    print(res)

