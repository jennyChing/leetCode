'''
423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
'''
import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
# store digits in dict
        #memo = collections.defaultdict(int)
        #for c in s:
        #    memo[c] += 1
        #for i, v in memo.items():
        #    if v == 'w'
# equals to:
        memo = collections.Counter(s)
        res = []
        for x in '0eroz 6six 7evens 5fiev 8eihtg 4ourf 3treeh 2tow 1neo 9nnei'.split():
            res.append(x[0] * memo[x[-1]])
            for c in x:
                memo[c] -= memo[x[-1]]
        return ''.join(sorted(res))

if __name__ == "__main__":
    s = "owoztneoer"
    res = Solution().originalDigits(s)
    print(res)
