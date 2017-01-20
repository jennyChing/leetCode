'''
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''
from math import ceil, log
class Solution(object):
    def rangeBitwiseAnd_math(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        b = (m ^ n).bit_length() # b is the digit of the most left diff bit
        b = int(log(m ^ n) // log(2)) + 1 # get the ceiling value
        m >>= b # eliminate the different part
        return m << b

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n: return m
        cnt, digits = 0, 1
        tmp = n
        while tmp > 1:
            digits += 1
            tmp >>= 1
        while digits > 1:
            if m < 2**(digits - 1):
                return cnt
            cnt += 2**(digits - 1) # most left digit is same
            m -= 2**(digits - 1)
            n -= 2**(digits - 1)
            cnt += self.rangeBitwiseAnd(m, n)
        return cnt

if __name__ == "__main__":
    res = Solution().rangeBitwiseAnd_math(13, 15)
    print(res)
