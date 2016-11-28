'''
318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
import collections
import itertools
import operator

class Solution(object):
    def maxProduct(self, words):
        mask_to_len = collections.defaultdict(int)
        print(mask_to_len)
        for word in words: # calculate all mask values first
            mask = sum(1 << (ord(c) - ord('a')) for c in set(word))
            print(mask_to_len[mask]) # initially is zero
            mask_to_len[mask] = max(mask_to_len[mask], len(word)) # only record the longest difference
        return max([mask_to_len[a] * mask_to_len[b] for a, b in itertools.combinations(mask_to_len, 2) if not a & b] or [0])

class oldSolution(object):
    def maxProduct(self, words):
        max_len = 0
        max_to_len = {} # use dict to avoid recalculate in the double for loop
        for i in range(len(words) - 1):
            if words[i] not in max_to_len: # calculate mask first
                max_to_len[i] = 0
                for c in set(words[i]):
                    max_to_len[i] += (1 << (ord(c) - ord('a')))
            for j in range(i + 1, len(words)):
                if words[j] not in max_to_len:
                    max_to_len[j] = 0
                    for c in set(words[j]):
                        max_to_len[j] += (1 << (ord(c) - ord('a')))
                mask1, mask2 = 0, 0
                mask1 |= max_to_len[i]
                mask2 |= max_to_len[j]
                if mask1 & mask2 == 0:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len

if __name__ == '__main__':
    res = Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
    print(res)


