'''
387. First Unique Character in a String  QuestionEditorial Solution

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        all_set = set()
        repeat_set = set()
        for c in s:
            if c in all_set:
                repeat_set.add(c)
            else:
                all_set.add(c)
        unique = all_set.difference(repeat_set)
        for i in range(len(s)):
            if s[i] in unique:
                return i
if __name__ == '__main__':
    print(Solution().firstUniqChar("loveleetcode"))
