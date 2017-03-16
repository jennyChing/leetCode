'''
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        print(l, r, mid)
        return mid if mid * mid < x else mid - 1

if __name__ == "__main__":
    res = Solution().mySqrt(17)
    print(res)
