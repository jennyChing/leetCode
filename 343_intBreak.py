from functools import reduce
class Solution(object):
    def integerBreak(self, n):
        '''
        bruce-force search
        '''
# data structure: list of list
        lst = [[n // t + (1 if i < n % t else 0) for i in range(t)] for t in range(2, n+1)]
        print(max([reduce(lambda x, y: x * y, lst)]))
        return max([reduce(lambda x,y: x*y, [n // t + (1 if i < n % t else 0) for i in range(t)]) for t in range(2, n+1)])
if __name__ == '__main__':
    res = Solution().integerBreak(10)
    print(res)
