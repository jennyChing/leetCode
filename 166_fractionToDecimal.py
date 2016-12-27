'''
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
'''
from decimal import *
import math
getcontext().prec = 1000
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        isCycle = False
        while remainder != 0:
            if remainder in seen:
                tail = tail[:seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
                isCycle = True
                break
            seen[remainder] = len(tail)
            print("remainder:", remainder)
            print(remainder, denominator)
            digit, remainder = divmod(remainder * 10, abs(denominator))
            print("remainder:", remainder)
            tail += str(digit)
        return sign + str(head) + '.' +  tail if len(tail) != 0 else sign + str(head)

if __name__ == "__main__":
    res = Solution().fractionToDecimal(1, 6)
    print(res)
