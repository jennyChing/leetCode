'''
395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''
import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnts = collections.Counter(s)
        res = l = r = 0
        invalid = [key for key, value in cnts.items() if value < k] # find all invalid chars as split boundaries
        window = collections.defaultdict(int)
        for r in range(1, len(s) + 1):
            window[s[r - 1]] += 1
            if s[r - 1] in invalid:
                while l < r:
                    check = [key for key, value in window.items() if value < k]
                    print(l, r, s[l:r], check)
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    if check == [s[r - 1]]:
                        res = max(res, r - l - 1)
                    l += 1
                    print(l, r, s[l:r], s[r - 1], check, window)
                l = r
                window = collections.defaultdict(int)
        #print(res, check, invalid)
        if res == 0:
            check = [key for key, value in window.items() if value < k]
            if not check:
                res = max(res, r - l)
        return res

    def longestSubstring_refer(self, s, k): # use recursive!!!
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0 # impossible
        cnts = collections.Counter(s)
        min_cnt = float('inf')
        invalid = [key for key, value in cnts.items() if value < k and value < min_cnt] # use appeared least invalid chars as split boundaries
        print(invalid)
        if not invalid:
            return len(s)
        return max(self.longestSubstring_refer(subs, k) for subs in s.split(invalid[-1]))


if __name__ == "__main__":
    s = "ababbc"
    k = 2
    s = "aaabbb"
    k = 3
    s = "baaacbd"
    k = 3
    res = Solution().longestSubstring_refer(s, k)
    print(res)
