'''
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
           "" c * a * b
        "" T  F T F T F
        a  F  F F T T F
        a  F  F F F T F
        b  F  F F F F T
        """
        dp = [[False for _ in range(1 + len(p))] for _ in range(1 + len(s))] # does p[:i] covers s[:j] (initially empty string "")
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*' # * can take zero!'

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], '.') and dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], '.')
        print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    res = Solution().isMatch("aab", "c*a*b")
    print(res)

