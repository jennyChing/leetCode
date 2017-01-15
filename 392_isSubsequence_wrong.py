'''
392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
'''
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
# MISS UNDERTANDING: this is for string matching from 演算法筆記


# calculate failure function (DP): O(s) time
        fail = [-1] * 100 # DP table storing prefix length; s max length is 100
        j = fail[0]
        for i in range(1, len(s)):
            while j >= 0 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]: # add length
                j += 1
            fail[i] = j

# start string matching: O(t) time
        j = -1
        for i in range(len(t)):
            while j >= 0 and s[j + 1] != t[i]:
                j = fail[j]
            if s[j + 1] == t[i]: # add length
                j += 1
            if j == len(t) - 1:
                j = fail[j]
            # print(i, "s index:", i - len(s) + 1)
        return j == len(s) - 1

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    res = Solution().isSubsequence(s, t)
    print(res)
