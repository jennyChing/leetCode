class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_s = {}
        dic_t = {}
        for c in s:
            if c in dic_s:
                dic_s[c] += 1
            else:
                dic_s[c] = 1
        for c in t:
            if c in dic_t:
                dic_t[c] += 1
            else:
                dic_t[c] = 1
        for k, v in dic_t.items():
            if k not in dic_s or v != dic_s[k]:
                return k
