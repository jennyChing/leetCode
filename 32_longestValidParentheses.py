'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
# idea: dp keep record of longest valid paretheses, look up s[i - curr]
        res  = hasLeft = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')' and hasLeft:
                dp[i] = dp[i - 1] + 2 # found a valid pair
                dp[i] += dp[i - dp[i]] if i - dp[i] >= 0 else 0 # If DP[i - 1] is not 0 means we have something like this “(())”
                res = max(res, dp[i])
                hasLeft -= 1
            elif s[i] == '(':
                hasLeft += 1
        return res

if __name__ == '__main__':
    res = Solution().longestValidParentheses("(()))()")
    print(res)
