class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        # [idea] While loop % 2 or 3 or 5 till not multiple of these numbers, then check if num == 1
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

