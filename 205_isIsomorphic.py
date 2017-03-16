class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s, dict_t = {}, {}
        for a, b in zip(s, t):
            if (a in dict_s and dict_s[a] != b) or (b in dict_t and dict_t[b] != a): # both have possibility to have new char!
                return False
            else:
                dict_s[a] = b
                dict_t[b] = a
        return True
