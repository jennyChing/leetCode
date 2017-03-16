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
	if len(a) < len(b):
            return self.addBinary(b, a)
        b = b.zfill(len(a))
        carry, res = 0, ""
        for i in range(len(a) - 1, -1, -1):
            d = ord(a[i]) + ord(b[i]) - 2 * 48 + carry
            carry = 1 if d > 1 else 0
            res += str(d % 2)
        res += '1' if carry else ''
        return res[::-1]
if __name__ == '__main__':
    res = Solution().addBinary("1", "111")
    print(res)
