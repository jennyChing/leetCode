'''
44. Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
	dp = [[False for _ in range(1 + len(p))] for _ in range(1 + len(s))] # does p[:i] covers s[:j] (initially empty string "")
        dp[0][0] = True
        if len(p) - p.count('*') > len(s):   #avoid TLE
            return False

        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] if p[j - 1] == '*' else False# * can be zero!'

        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], '?')
        return dp[-1][-1]



if __name__ == '__main__':
    s = "aa"
    p = "a"
    res = Solution().isMatch(s, p)

