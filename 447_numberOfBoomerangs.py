'''
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''
import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(points)):
            dist = collections.defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    a, b, c, d = points[i][0], points[i][1], points[j][0], points[j][1]
                    distance = (a - c) ** 2 + (b - d) ** 2 # no need to **(0.5)
                    if distance in dist and dist[distance] > 0:
                        cnt += dist[distance] * 2
                    dist[distance] += 1
        return cnt


if __name__ == "__main__":
    points = [[0,0],[1,0],[2,0]]
    res = Solution().numberOfBoomerangs(points)
    print(res)
