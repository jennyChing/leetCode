'''
504. Base 7
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sign = -1 if num < 0 else 1
        num = abs(num)
        res  = ""
        while num >= 7:
            res += str(num % 7)
            num //= 7
        res += str(num % 7)
        res += "" if sign == 1 else "-"
        return res[::-1]
if __name__ == '__main__':
    res = Solution().convertToBase7(101)
    print(res)
