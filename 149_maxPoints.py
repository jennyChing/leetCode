'''
149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import collections
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
	# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from decimal import *
getcontext().prec = 10
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcd(x, y):
            if x > y:
                return gcd(y, x)
            sign = -1 if x * y < 0 else 1
            x, y = abs(x), abs(y)
            while y:
                r = x % y
                x = y
                y = r
            return sign * x

        if len(points) < 2:
            return len(points)
        # idea: keep a hashtable O(n^2) every 2 points calculate line, first need to count number of duplicated points
        duplicate = collections.defaultdict(int)
        uni_points = []
        for p in points:
            if (p.x, p.y) not in duplicate:
                uni_points.append(p)
            duplicate[(p.x, p.y)] += 1

        memo = collections.defaultdict(list)
        for i in range(len(uni_points)):
            for j in range(i + 1, len(uni_points)):
                p1, p2 = uni_points[i], uni_points[j]
                m = float(p2.y - p1.y) / float(p2.x - p1.x) if p1.x - p2.x != 0 else float('inf')
                k = p1.y - m * p1.x if p1.x - p2.x != 0 else p1.x # 截距
                m_gcd = gcd(p2.y - p1.y, p2.x - p1.x)
                if p1.x - p2.x != 0:
                    sign = "-" if (p2.y - p1.y) * (p2.x - p1.x) < 0 else ""
                m_key = sign + str(abs((p2.y - p1.y) / m_gcd)) + '/' + str(abs((p2.x - p1.x) / m_gcd)) if p1.x - p2.x != 0 else float('inf')
                if (m_key, k) in memo and (p2.x, p2.y) in memo[(m_key, k)]: # on same line and p1 visited: skip this pair!
                    continue
                if (p1.x, p1.y) not in memo[(m_key, k)]:
                    memo[(m_key, k)] += [(p1.x, p1.y)] * duplicate[(p1.x, p1.y)]
                memo[(m_key, k)] += [(p2.x, p2.y)] * duplicate[(p2.x, p2.y)]
        return len(memo[max(memo, key=lambda k: len(memo[k]))]) if memo else max(duplicate.values())

if __name__ == '__main__':
    points = [[1,2], [3,4]]
    res = Solution().maxPoints(points)
    print(res)

