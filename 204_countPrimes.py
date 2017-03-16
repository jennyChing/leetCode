class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [True] * n # 2 * i + 1= n
        isPrime[0], isPrime[1] = False, False
        res = 1
        for i in range(3, n, 2): # jump only to check odd numbers
            if isPrime[i]:
                res += 1
                for j in range(i * i, len(isPrime), i):
                    isPrime[j] = False
        return res
