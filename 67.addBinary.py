'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        add three ppl: a, b, and carry (either 0 or 1)
        """
        res = ""
        i, carry = 0, 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            if i < min(len(a), len(b)):
                if int(a[i]) + int(b[i]) + carry > 1:
                    res += str((int(a[i]) + int(b[i]) + carry - 2))
                    carry = 1
                else:
                    res += str((int(a[i]) + int(b[i]) + carry))
                    carry = 0
                print("both: ", res)
            elif i >= len(a):
                if int(b[i]) + carry > 1:
                    res += str((int(b[i]) + carry - 2))
                    carry = 1
                else:
                    res += str((int(b[i]) + carry))
                    carry = 0
                print("b :", res)
            elif i >= len(b):
                if int(a[i]) + carry > 1:
                    res += str((int(a[i]) + carry - 2))
                    carry = 1
                else:
                    res += str((int(a[i]) + carry))
                    carry = 0
                print("a :", res)
        print(len(" "))
        if carry:
            res += str(carry)
        return res[::-1]
if __name__ == '__main__':
    res = Solution().addBinary("1", "111")
    print(res)
