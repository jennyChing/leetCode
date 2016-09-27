'''
326. Power of Three  QuestionEditorial Solution

Given an integer, write a function to determine if it is a power of three.
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 3:
            for t in temp:
                memo[t] = True
        if n in memo:
            return memo[n]
        elif n % 3 != 0:
            memo[n] = False
        else:
            temp.append(n)
            Solution().isPowerOfThree(n//3)
        return memo[n]

if __name__ == '__main__':
    memo = {3: True}
    temp = []
    print(Solution().isPowerOfThree(8))
