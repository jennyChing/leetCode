'''
careful for the overflow issue (return 0)
use the tehnique to deal with negative numbers
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: # important technique! make your code simplier
            return -self.reverse(-x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10

        return res if res <= 0x7fffffff else 0
