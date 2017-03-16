class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        arr_str = str.split()
        p_dict, s_dict = {}, {}
        if len(arr_str) != len(pattern):
            return False
        for p, s in zip(pattern, arr_str):
            if (p in p_dict and p_dict[p] != s) or (s in s_dict and s_dict[s] != p):
                return False
            else:
                p_dict[p] = s
                s_dict[s] = p
        return True
