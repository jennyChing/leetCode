'''
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(s) < len(p): return res
        memo_p = [0] * 123 # max length of p is 123
        memo_s = [0] * 123 # max length of s is 123
# initial check for anagram with the first p elements of s
        for c in s[:len(p) - 1]:
            memo_s[ord(c)] += 1
        for c in p:
            memo_p[ord(c)] += 1

# O(mn) to O(n): use sliding window!
        for i in range(len(p) - 1, len(s)):
            memo_s[ord(s[i])] += 1
            if i > len(p) - 1:
                memo_s[ord(s[i - len(p)])] -= 1
            if memo_p == memo_s:
                res.append(i - len(p) + 1)
        return res

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    res = Solution().findAnagrams(s, p)
    print(res)
