'''
43. Multiply Strings

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        x, y = 0, 0
        for n in num1:
            x *= 10
            x += ord(n) - ord("1") + 1
        for n in num2:
            y *= 10
            y += ord(n) - ord("1") + 1
        res, mul = "", x * y
        while mul > 0:
            res += chr(mul % 10 + 48)
            mul //= 10
        return res[::-1]

if __name__ == "__main__":
    res = Solution().multiply("123", "456")
    print(res)
