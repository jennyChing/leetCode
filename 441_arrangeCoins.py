'''
441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if (mid + 1) * mid / 2 == n:
                return mid
            elif (mid + 1) * mid / 2 > n:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1 if (l + 1) * l / 2 > n else l

if __name__ == "__main__":
    res = Solution().arrangeCoins(8)
    print(res)

