class Solution(object):
    def recursive(self, n, memo, temp):
        print(n, temp)
        if n == 4:
            print(temp)
            for t in temp:
                memo[t] = True
        if n in memo:
            return memo[n]
        elif n % 4 != 0:
            memo[n] = False
            for t in temp:
                memo[t] = False
        else:
            temp.append(n)
            Solution().recursive(n//4, memo, temp)

    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = {0: False, 1: True, 4: True}
        temp = []
        Solution().recursive(n, memo, temp)
        print(memo)
        return memo[n]


