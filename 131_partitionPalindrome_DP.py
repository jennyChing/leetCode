'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
# use DP table to record the substrings
        self.memo = [None] * (len(s) + 1)
        self.memo[0]=[[]]
        return self.__directed_partition(s)

    def __directed_partition(self, s):
        s_len = len(s)
        if self.memo[s_len]:
            return self.memo[s_len] # avoid repeat calling
        res = []

    # for loop start checking from the back
        for i in range(len(s) - 1, -1, -1):
            curr = s[i:] # cut s into two parts by index i
            print(curr)
            if curr == curr[::-1]: # check palindrome here
                print("givin next", s[:i])
                prefix = self.__directed_partition(s[:i])
                res += [r + [curr] for r in prefix]
        self.memo[s_len] = res
        return res

if __name__ == "__main__":
    res = Solution().partition("aab")
    print(res)
