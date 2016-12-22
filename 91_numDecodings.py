'''
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        res = [0 for _ in range(len(s))] + [1]
        if s[-1] != '0':
            res[-2] = 1
        for i in range(len(s) - 2, -1, -1):
            if int(s[i]) != 0:
                res[i] += res[i + 1]
                if int(s[i:i + 2]) < 27:
                    res[i] += res[i + 2]
        return res[0]

if __name__ == "__main__":
    s = "32121"
    res = Solution().numDecodings(s)
    print(res)
