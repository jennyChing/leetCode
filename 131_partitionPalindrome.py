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
        def __directed_checkPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

# Split the string into n substrings with recursive function
        res, subs = [], []
        def __directed_dfs(res, level, subs, target_len):
            print(subs, target_len)

            # Check if all temps is palindrome (no one passed because invalid)
            if target_len == len(s):
                res.append([subs])
            # start for loop with the new level
            for i in range(1, len(s) + 1):
                if level + i > len(s): # control the length of substring temp
                    break
                temp = s[level:level + i] # all possible substrings
                if not __directed_checkPalindrome(temp):
                # won't append this substring so that this level's target_len won't be matched
                    continue
                __directed_dfs(res, i + level, subs + [temp], target_len + len(temp))

        __directed_dfs(res, 0, subs, 1)
        return res

if __name__ == "__main__":
    res = Solution().partition("aab")
    print(res)
