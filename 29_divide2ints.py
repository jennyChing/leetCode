'''
29. Divide Two Integers

Divide two integers without using multiplication, division and mod operator.
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        endIsNeg = True if dividend < 0 else False
        sorIsNeg = True if divisor < 0 else False
        dividend = abs(dividend)
        divisor = abs(divisor)

        vals = []
        while dividend >= divisor:
            vals.append(divisor)
            divisor += divisor
        result = 0
        for i in range(len(vals) - 1, -1, -1):
            if dividend >= vals[i]:
                dividend -= vals[i]
                result += 1 << i
        print(dividend, i, result)

        if endIsNeg ^ sorIsNeg:
            return result * -1
        return result

if __name__ == "__main__":
    res = Solution().divide(1, 1)
    print(res)
