'''
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''
import collections
import heapq
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
# idea: use dict {'char': list of index} to record and when t is covered, calculate the  window size, if repeated, replace oldest with newest index
        memo = collections.defaultdict(list)
        t_cnt = collections.Counter(t)
        missing = sum(t_cnt.values())
        cachedIdx = []
        minWin, start, end = len(s), 0, len(s) - 1
        for i, c in enumerate(s):
            if c in t_cnt:
                memo[c].append(i) # add in this index to the valid list!
                cachedIdx.append(i)
                if t_cnt[c] > 0:
                    t_cnt[c] -= 1 # clear char in t
                    missing -= 1
                else:
                    cachedIdx.remove(memo[c][0])
                    del memo[c][0] # replaced with later index
                if missing == 0:
                    minI, maxI = cachedIdx[0], cachedIdx[-1]
                    if maxI - minI < minWin:
                        start, end = minI, maxI
                        minWin = maxI - minI
        return s[start:end + 1] if missing == 0 else ""

if __name__ == '__main__':
    res = Solution().minWindow("ADOBECODEBANC", "ABC")
    # res = Solution().minWindow("ab", "b")
    print(res)

