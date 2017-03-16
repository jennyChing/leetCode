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
	memo = collections.Counter(s)
        for i, c in enumerate(s):
            if memo[c] == 1:
                return i
        return -1

    def firstUniqChar_faster(self, s):
        """
        :type s: str
        :rtype: int
        """
# loop through 26 alphebets (O(1))
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])

if __name__ == '__main__':
    print(Solution().firstUniqChar("loveleetcode"))
