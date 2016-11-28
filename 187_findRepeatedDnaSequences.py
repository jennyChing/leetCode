'''
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].
'''
import collections

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        memo = collections.defaultdict(list)
        n = len(s)
        bits = {'A':0, 'C':1, 'G':2, 'T':3}
        # O(m) first calcualte hashkey int for idx 0 ~ 9 with 4 bits represented mask
        mask = 0
        res = []
        for i in range(10):
            mask *= 4
            mask += bits[s[i]]
        memo[mask] += 1

        for i in range(10, n): # O(n) for loop calculate all hashkeys
            mask = mask - bits[s[i - 10]] * (4**9)
            mask = mask * 4 + bits[s[i]]
            memo[mask] += 1
        return res


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    res = Solution().findRepeatedDnaSequences(s)
    print(res)
