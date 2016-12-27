'''
306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
'''
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)): # len b and c + 1 if no match last run
                a, b = num[:i], num[i:j]
                c = str(int(a) + int(b))
                if (len(a) != 1 and a[0] == '0') or (len(b) != 1 and b[0] == '0'):
                    continue
                if num[j:].startswith(c):
                    a, b = b, c
                    c_idx = j + len(c)
                    while c_idx < len(num):
                        c = str(int(a) + int(b))
                        if c_idx + len(c) <= len(num) and num[c_idx:c_idx + len(c)] == c:
                            a, b = b, c
                            c_idx += len(c)
                        else:
                            break
                    if c_idx == len(num):
                        return True
        return False


if __name__ == "__main__":
    num = "112358"
    num = "199100199"
    num = "1023"
    res = Solution().isAdditiveNumber(num)
    print(res)
