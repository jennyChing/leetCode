class Solution(object):
    def convertToTitle(self, n):
        res = ""
        while n >= 1:
            last = (n - 1) % 26 + ord('A')
            print(last, n, chr(last), res)
            res = chr(last) + res
            n = (n - 1) // 26
        return res
if __name__ == '__main__':
    res = Solution().convertToTitle(27)
    print(res)
