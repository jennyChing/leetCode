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
        while n > 3:
            if n % 3:
                return False
            n /= 3
        return n == 1 or n == 3

    def isPowerOfThree_refer(self, n):
        """
        :type n: int
        :rtype: bool
        """
# not using loops and recursion
        return n > 0 and pow(3 ,int(log(0x7FFFFFFF)/log(3))) % n == 0

if __name__ == '__main__':
    memo = {3: True}
    temp = []
    print(Solution().isPowerOfThree(8))
