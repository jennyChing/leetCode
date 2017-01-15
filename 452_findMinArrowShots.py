'''
452. Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
'''
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        overlap = []
        for i in range(len(points)):
            for j in range(i):
                if points[i][0] <= points[j][1]:
                    overlap.append([points[i][0], min(points[i][1], points[j][1])])
        if len(overlap) == 0:
            return len(points)
        if len(overlap) == 1:
            return len(points) - 1
        cleaned = [] if overlap[1][0] <= overlap[0][1] else [overlap[0]]
        for i in range(1, len(overlap)):
            if overlap[i] == overlap[i - 1]:
                continue
            elif overlap[i][0] <= overlap[i - 1][1]:
                cleaned.append([overlap[i][0], min(overlap[i][1], overlap[i - 1][1])])
            else:
                cleaned.append(overlap[i])
        print(cleaned, overlap)
        return len(cleaned)

if __name__ == "__main__":
    points = [[10,16], [2,8], [1,6], [7,12]]
    res = Solution().findMinArrowShots(points)
    print(res)
