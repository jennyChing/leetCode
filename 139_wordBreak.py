'''
139. Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict
        :rtype: bool
        """
# find the max len of word in the wordDict so that everytime looking at most len of characters
        max_word_len = 0
        for v in wordDict:
            max_word_len = max(max_word_len, len(v))

        DP = [False for _ in range(len(s) + 1)]
        DP[0] = True # empty string
        for i in range(1, 1 + len(s)):
            for j in range(i):
                print(i,j)
                if len(s[j:i]) > max_word_len:
                    continue
                print(s[j:i])
                if DP[j] and s[j:i] in wordDict:
                    DP[i] = True
                    print(DP)
                    break
        return DP[-1]

# iteratively look back substring 0 ~ max_word_len characters to see if any word from dict is matched
        #def __directed_dfs(idx, visited):
        #    print(idx, len_i)
        #    pir
        #    if idx == len_i:
        #        return True
        #    if visited[idx]:
        #        print(idx, len_i)
        #        return False
        #    for i in range(1, len(s) + 1):
        #        print(i, s[idx:i])
        #        if s[idx:i] in wordDict:
        #            return __directed_dfs(idx + 1, visited)
        #    visited[idx] = True
        #    return False

        #return __directed_dfs(0, [False for _ in range(len(s))])

if __name__ == "__main__":
    s = "aleetcode"
    wordDict = {"a", "leet", "code"}
    res = Solution().wordBreak(s, wordDict)
    print(res)
