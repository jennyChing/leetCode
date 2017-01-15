'''
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        dp = [0] * n # first one is always 0
        i, j = 1, 0
        while i < n:
            if str[i] == str[j]:
                dp[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = dp[j - 1]
                else:
                    dp[i] = 0
                    i += 1
        if dp[-1] and n % (n - dp[-1]) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    str = "abcabcabcabc"
    res = Solution().repeatedSubstringPattern(str)
    print(res)
