'''
467. Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string strings.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
'''
import collections
import string
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        memo = collections.defaultdict(int)
        wraparound = "z" + string.ascii_lowercase
        subStr, memo[p[0]] = 1, 1 # init substring len and char stored in memo
        for i in range(1, len(p)):
            subStr = subStr + 1 if p[i - 1:i + 1] in wraparound else 1
            print(p[i - 1:i + 1], subStr)
            memo[p[i]] = max(subStr, memo[p[i]]) if p[i] in memo else subStr
            print(memo)
        return sum(memo.values())

if __name__ == "__main__":
    p = "zab"
    res = Solution().findSubstringInWraproundString(p)
    print(res)
