import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # use counter is slow!
        memo_s, memo_t = collections.Counter(s), collections.Counter(t)
        if memo_s == memo_t:
            return True
        return False

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return s.sort() == t.sort()
