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
        # idea: keep a hashtable O(n^2) every 2 points calculate line
        memo = collections.defaultdict(int)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if p1.x - p2.x == 0:
                    memo[float('inf')] += 1
                else:
                    memo[(p2.y - p1.y)/(p2.x - p1.x)] += 1

        return max(memo.values())

if __name__ == '__main__':
    points = [[1,2], [3,4]]
    res = Solution().maxPoints(points)
    print(res)

