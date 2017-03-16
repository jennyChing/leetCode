'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            dp[i][0] = i
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for i in range(1, 1 + len(word2)):
            for j in range(1, 1 + len(word1)):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if word2[i - 1] != word1[j - 1] else dp[i - 1][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    res = Solution().minDistance("ajced", "abcdef")
    print(res)

