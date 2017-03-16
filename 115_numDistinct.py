'''
115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
# idea: if t[i] != s[j]:dp[i][j] = dp[i][j - 1] else dp[i - 1][j - 1] + dp[i][j - 1], dp recording the number of ways that t can be formed in s
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
        for i in range(len(s)):
            dp[0][i] = 1 # t is "" empty string so can form every substring s
        for i in range(len(t)):
            for j in range(len(s)):
                dp[i][j] = dp[i][j - 1] if t[i] != s[j] else dp[i][j - 1] + dp[i - 1][j - 1]
        print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    res = Solution().numDistinct("rabbbit", "rabbit")
    print(res)

