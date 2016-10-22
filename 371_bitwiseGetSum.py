'''
371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''
class Solution(object):
    def getSum(self, a, b):
    # 32-bit number with all bits set to one (max int) as sum base
        mask = 0xFFFFFFFF # ~4bn
        print(mask)
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1 & mask)
            print(a, b, mask)
        # 0x7FFFFFFF is the max int (~2bn)
        return a if a < 0x7FFFFFFF else ~(a ^ mask)
if __name__ == '__main__':
    res = Solution().getSum(3,5)
    print(res)

