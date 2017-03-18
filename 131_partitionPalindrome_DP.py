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
        def __directed_partition(s):
            s_len = len(s)
            if memo[s_len]:
                return memo[s_len] # avoid repeat calling
            res = []
            for i in range(len(s) - 1, -1, -1): # for loop split by the back
                curr = s[i:] # cut s into two parts by index i
                print("split:", curr)
                if curr == curr[::-1]: # check palindrome here
                    print("givin next", s[:i])
                    prefix = __directed_partition(s[:i])
                    res += [r + [curr] for r in prefix]
            memo[s_len] = res
            print(memo)
            return res
        memo = [0] * (len(s) + 1)
        memo[0]=[[]]
        return __directed_partition(s)


if __name__ == "__main__":
    res = Solution().partition("aab")
    print(res)
