'''
202. Happy Number  QuestionEditorial Solution
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
memo = {1: True}
class Solution(object):
    def recursive(self, n, temp):
        '''
        :type n: int
        :rtype: bool
        '''
        temp.append(n)
        print(n, temp)
        digits = []
        while n > 9:
            digits.append(n % 10)
            n = n // 10
        digits.append(n % 10)
        d_sum = 0
        for d in digits:
            d_sum += d * d
        print(n, digits, d_sum, temp)
        if d_sum == 1:
            for t in temp:
                memo[t] = True
            return True
        elif d_sum < 10:
            for t in temp:
                memo[t] = False
            return False
        Solution().recursive(d_sum, temp)

    def isHappy(self, n):
        '''
        :type n: int
        :rtype: bool
        '''
        if n in memo:
            return memo[n]
        temp = []
        Solution().recursive(n, temp)
        return memo[n]

    def isHappy_2(self, n):
        '''
        :type n: int
        :rtype: bool
        '''
	memo = set()
        while n != 1 and n not in memo:
            memo.add(n)
            tmp = (n % 10) ** 2
            while n > 9:
                n //= 10
                tmp += (n % 10) ** 2
            n = tmp
        return n == 1

if __name__ == '__main__':
    Solution().isHappy(19)
    print(memo)
