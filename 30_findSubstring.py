'''
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''
import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res, perm = [], []
        def permutation(partial, visited):
            if len(partial) == len(words):
                perm.append(partial)
                return
            for i, w in enumerate(words):
                if i in visited:
                    continue
                visited.add(i)
                permutation(partial + [w], visited)
                visited.remove(i)
        permutation([], set())
        wlist = []
        for p in perm:
            wlist.append("")
            for i in range(len(p)):
                wlist[-1] += p[i]
        for i in range(len(s)):
            for v in wlist:
                if s[i:].startswith(v):
                    res.append(i)
        return res

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # idea: Using a counter and a sliding window, we push the window from left to right, counting the number of valid words in the window. When the number of a word in the window is more than the times it appears in words or we meet a invalid word, push the window.
        if not words: return []
        m, n = len(words), len(words[0]) # all words of the same length
        cnt = collections.Counter(words)
        res = []
        # sliding window loop k as start index (start at most from n - 1)
        for k in range(n):
            startIdx = k
            subd = collections.defaultdict(int)
            count = 0
            # loop over string s
            for j in range(k, len(s) - n + 1, n): # each step move n
                word = s[j:j + n] # fix len of n
                if word in cnt: # check if following [j:j+n] is valid word
                    subd[word] += 1
                    count += 1
                    # Shift the window as long as we have encountered more number of a word than is needed
                    while subd[word] > cnt[word]: # valid word but too much!
                        print(subd, cnt, startIdx, n)
                        subd[s[startIdx:startIdx + n]] -= 1 #remove from start
                        startIdx += n # get rid of words if valid but too much
                        count -= 1
                    if count == m: # Count will be equal to m only when we all the words are read the exact number of times needed
                        res.append(startIdx)
                # If is not a valid word then just skip over the current word (Don't worry about the middle characters
                else: # word subset is not valid, not exist in words
                    startIdx = j + n # reset start index
                    subd = collections.defaultdict(int) # reset substitute dict
                    count = 0 # count restarts from 0
        return res

if __name__ == '__main__':
    s = "gbarbarfoothefoobarman"
    words = ["foo", "bar"]
    res = Solution().findSubstring(s, words)
    print(res)

