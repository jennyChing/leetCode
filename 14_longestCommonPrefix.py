'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i] or i >= len(s):
                    return strs[0][:i]
        return strs[0]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # deal with different length of strs
        common = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(common):
                if j >= len(strs[i]) or strs[i][j] != common[j]:
                    common = common[:j]
                j += 1
        return common


if __name__ == '__main__':
    strs = ["a"]
    res = Solution().longestCommonPrefix(strs)
    print(res)
