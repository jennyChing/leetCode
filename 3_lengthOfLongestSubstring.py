'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = res = 0
        memo = {}
        for j in range(len(s)):
            if s[j] in memo and i <= memo[s[j]]: # when starting index equals need to update too
                print(memo, i, memo[s[j]], j)
                i = memo[s[j]] + 1 # update the starting pointer
            else:
                res = max(res, j - i + 1) # otherwise just check the max length currently
            memo[s[j]] = j # will cover the old char so no need to handle it when repeated
        # last one
        return res

if __name__ == "__main__":
    s = "pwwkew"
    s = "dvdf"
    s = "abba"
    s = "abcabcbb"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
