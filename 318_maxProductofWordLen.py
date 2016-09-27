class Solution(object):
    def maxProduct(self, words):
        max_len = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                mask1, mask2 = 0, 0
                for c in set(words[i]):
                    mask1 |= (1 << (ord(c) - ord('a')))
                for c in set(words[j]):
                    mask2 |= (1 << (ord(c) - ord('a')))
                print(words[i], words[j], "same?", mask1 & mask2 == 0)
                if mask1 & mask2 == 0:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
                    print(max_len)
        return max_len
if __name__ == '__main__':
    res = Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
    print(res)


