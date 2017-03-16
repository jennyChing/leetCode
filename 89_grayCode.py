'''
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        successive values differ in only 1 bit means "+ 2 ** n"
        """
        res = [0]
        for i in range(n):
            for n in reversed(res):
                res.append(n + 2 ** i)
        return res

if __name__ == "__main__":
    res = Solution().grayCode(3)
    print(res)
