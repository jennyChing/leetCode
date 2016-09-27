'''
371. Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        use bitwise to solve the problem
        """
        mask = 0xFFFFFF
        print(type(mask), mask)

if __name__ == '__main__':
    Solution().getSum(10, 3)
