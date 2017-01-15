'''
436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        mapping = {} # record the original order before sorting
        for i in range(len(intervals)):
            mapping[intervals[i].start] = i
        intervals = sorted(intervals, key=lambda x: x.start)
        res = {} # need map to original order
        for i in range(len(intervals)):
            # do binary search to find the min-right start point:
            l, r = i, len(intervals) - 1
            while l < r:
                mid = (l + r) // 2
                print(i, mid)
                if intervals[i].end <= intervals[mid].start:
                    r = mid
                else:
                    l = mid + 1
            if intervals[i].end <= intervals[l].start and l != i:
                res[mapping[intervals[i].start]] = mapping[intervals[l].start]
            else:
                res[mapping[intervals[i].start]] = -1
        return [res[i] for i in range(len(intervals))]

if __name__ == "__main__":
    intervals = [ Interval(1,4), Interval(2,3), Interval(3,4)]
    res = Solution().findRightInterval(intervals)
    print(res)
