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
            check = strs[0][i]
            for s in strs:
                print(s, i, strs[0])
                if s[i] != check or i >= len(s):
                    return strs[0][:i]
        return strs[0]
if __name__ == '__main__':
    strs = ["a"]
    res = Solution().longestCommonPrefix(strs)
    print(res)
