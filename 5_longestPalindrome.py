'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def __find_pal(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        max_pdm = ""
        for i in range(len(s)):
            odd = __find_pal(i, i)
            if len(odd) > len(max_pdm):
                max_pdm = odd
            even = __find_pal(i, i + 1)
            if len(even) > len(max_pdm):
                max_pdm = even

        return max_pdm

if __name__ == "__main__":
    res = Solution().longestPalindrome("cbbd")
    print(res)
