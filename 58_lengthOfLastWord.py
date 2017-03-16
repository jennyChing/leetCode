'''
58. Length of Last Word
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
	if not s:
            return 0
        s, res = s[::-1], 0
        for c in s:
            if c != " ":
                res += 1
            elif res:
                return res
        return res

if __name__ == '__main__':
    s = "a "
    res = Solution().lengthOfLastWord(s)
    print(res)
