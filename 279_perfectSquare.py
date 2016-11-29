'''
279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

DP, simillar to #343
'''
class Solution(object):
    dp = [0] # store it as class variable to reduce repeated calculation
    print(dp)
    def numSquares(self, n):
# using for loop to solve DP (simillar to coin change method)
        max_sqrt = int(n**(0.5))
        start = len(self.dp)
        if len(self.dp) >= n:
            return self.dp[n]
        else:
            self.dp += [float('inf')] * (n + 1 - len(self.dp))
            for i in range(start, n + 1):
                if i**(0.5) % 1 == 0:
                    self.dp[i] = 1
                for j in range(1, max_sqrt + 1):
                    self.dp[i] = min(self.dp[i], self.dp[i - j * j] + 1)
            print(self.dp, len(self.dp))
        return self.dp[n]
# record the length of combination in a matrix
       # record = [[0 for i in range(max_sqrt)] for j in range(max_sqrt)]
       # for i in range(1, max_sqrt + 1):
       #     temp = n
       #     print(i)
       #     for j in range(i, 0, -1):
       #         while temp - j * j >= 0:
       #             print(temp)
       #             temp -= j * j
       #             print(record)
       #             record[i - 1][j - 1] += 1
       # print(record)
       # return min([sum(i) for i in record])
if __name__ == '__main__':
    n = 48
    res = Solution().numSquares(n)
    print(res)

