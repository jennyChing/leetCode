# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    return version >= 2

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        find the earliest True with binary search
        """
        left, right = 1, n
        while right > left:
            mid = (right + left) // 2
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
        return left
if __name__ == '__main__':
    res = Solution().firstBadVersion(2)
    print(res)
