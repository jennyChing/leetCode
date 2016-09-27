class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        dynamic programming: identify cases that cannot win with given n
        """
        if n % 4 == 0:
            return False
        return True
