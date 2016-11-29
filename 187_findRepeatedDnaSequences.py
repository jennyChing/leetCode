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
        memo = collections.defaultdict(int)
        n = len(s)
        if n < 10:
            return []
        bits = {'A':0, 'C':1, 'G':2, 'T':3}
        # O(m) first calcualte hashkey int for idx 0 ~ 9 with 4 bits represented mask
        mask = 0
        res = []
        for i in range(9):
            mask *= 4
            mask += bits[s[i]]

        for i in range(9, n): # O(n) for loop calculate all hashkeys
            # mask = mask - bits[s[i - 10]] * (4**9) # drop old idx
            mask = mask * 4 + bits[s[i]] # add current idx
            mask &= 0xfffff # 16 進位填滿來消掉 old index number
            memo[mask] += 1
            if memo[mask] == 2:
                res.append(s[i - 9:i + 1])
        return res


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    res = Solution().findRepeatedDnaSequences(s)
    print(res)
