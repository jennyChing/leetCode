'''
405. Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
'''
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        if num < 0: num += 2 ** 32
        res = ""
        digits = "0123456789abcdef"
        while num > 15:
            d = num % 16
            num //= 16
            res += digits[d]
        res += digits[num]
        return res[::-1]


if __name__ == "__main__":
    res = Solution().toHex(-1)
    print(res)
