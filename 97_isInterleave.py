'''
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
          a a b c c
        d T T T F F
        b F F T T T
        b F F T T F
        c F F F T T
        a F F F F T
        """
        if len(s2) + len(s1) != len(s3):
            return False
# idea: records could s1[:i] and s2[:j] form s3[:i + j], T if s1[i] or s2[j] = s3[i + j]
        dp = [[True for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)] # initial is True to form empty string ""
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1] # up is True and idx i - 1 of s1 and s3 is the same
        print("first")
        print(dp)
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1] # left is True and idx j - 1 of s1 and s3 is the same
        print("second")
        print(dp)
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j]) # up or left is valid
        print("last")
        print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac" # aa(1) db(2) bc(1) bca(2) c(1)
    res = Solution().isInterleave(s1, s2, s3)
    print(res)

