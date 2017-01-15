'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res, carry = "", 0
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(max(len(num1), len(num2))):
            d_sum = carry
            if i < len(num1):
                d_sum += ord(num1[i]) - ord('0')
            if i < len(num2):
                d_sum += ord(num2[i]) - ord('0')
            res += str((d_sum) % 10)
            carry = 0 if d_sum < 10 else 1
        if carry == 1:
            res += '1'
        return res[::-1]

if __name__ == "__main__":
    num1, num2 = "9", "99"
    res = Solution().addStrings(num1, num2)
    print(res)
