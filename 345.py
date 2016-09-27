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
        set_vow = set()
        arr_vow = ["a", "b", "c", "d", "e"]
        for v in arr_vow:
            set_vow.add(v)
        a, b = 0, len(s) - 1
        while a <= b:
            print("a", a, s[a])
            print("b", b, s[b])
            if s[a] in set_vow and s[b] in set_vow:
                print(s)
                tmp_a, tmp_b = s[a], s[b]
                s[a] = "e"
                s[b] = tmp_a
                print(s)
                a += 1
                b -= 1
            elif s[a] not in set_vow:
                a += 1
            elif s[b] not in set_vow:
                b -= 1
        return s
if __name__ == '__main__':
    Solution().reverseVowels("leetcode")

