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
        s = ' ' + s[::-1]
        print(s)
        isWord = False
        start, end = 0, len(s)
        i = 0
        while i < len(s) and isWord == False:
            if s[i] != ' ':
                isWord = True
                start = j = i
                print(start, j, i)
                while j < len(s) and isWord == True:
                    if s[j] == ' ':
                        isWord = False
                        end = j
                        break
                    j += 1
            i += 1
        print(end, start)
        return end - start
if __name__ == '__main__':
    s = "a "
    res = Solution().lengthOfLastWord(s)
    print(res)
