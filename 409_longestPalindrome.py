'''
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        memo = set()
        for c in s:
            if c in memo:
                cnt += 2
                memo.remove(c)
            else:
                memo.add(c)
        if memo:
            cnt += 1
        return cnt

import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cnt = collections.Counter(s)
        for k, v in cnt.items():
            if not v % 2:
                res += v
            elif (v - 1) > 0:
                res += v - 1
        if len(s) != res:
            res += 1
        return res

    def refer(self, s):
	odds = sum(v & 1 for v in collections.Counter(s).values())
    	return len(s) - odds + bool(odds)


if __name__ == "__main__":
    s = "abccccdd"
    res = Solution().longestPalindrome(s)
    print(res)
