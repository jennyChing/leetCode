class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        order is the key
        """
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, curr + prev
        return curr
