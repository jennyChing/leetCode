class Solution(object):
    def countBits(self, num):
        res = [0]
        while len(res) <= num:
            res.extend([x + 1 for x in res])
            print(res)
        return res[:num + 1]
if __name__ == '__main__':
    res = Solution().countBits(5)
    print(res)
