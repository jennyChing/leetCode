'''
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea: dp table record
        dp = [0 for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1): # reverse, down be updated first
            dp[i] = 1
            pre = dp[i]
            for j in range(i + 1, len(s)): # left should be updated first
                tmp = dp[j] # cache the value
                if s[i] != s[j]:
                    dp[j] = max(dp[j], dp[j - 1])
                else:
                    dp[j] = pre + 2 if j >= i + 2 else 2
                pre = tmp
        return dp[-1]
if __name__ == '__main__':
    res = Solution().longestPalindromeSubseq("bbbab")
    print(res)

