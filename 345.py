'''
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_vow = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] )
        front = []
        end = []
        i, j = 0, len(s) - 1
        if len(s) < 2:
            return s
        while i < j:
            if s[i] in set_vow and s[j] in set_vow:
                front.append(s[j])
                end.append(s[i])
                i += 1
                j -= 1
            else:
                if s[i] not in set_vow:
                    front.append(s[i])
                    i += 1
                elif s[j] not in set_vow:
                    end.append(s[j])
                    j -= 1
        if i == j:
            end.append(s[j])
        return ''.join(front + end[::-1])

if __name__ == '__main__':
    Solution().reverseVowels("leetcode")

