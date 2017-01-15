'''
435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
# sort the intervals and if former end > next interval's start, need to remove one of the interval to erase overlapping
        intervals.sort(key=operator.attrgetter('start', 'end'))
        cnt = 0
        pre, curr, nxt = 0, 1, 2
        while curr < len(intervals) - 1: # moving window size of 3
            # every move of the window check i - 1 and i + 1
            if intervals[pre].end > intervals[curr].start : # need remove
                cnt += 1 # must delete one, only difference is updating pre
                if intervals[curr].end > intervals[nxt].start:
                    pre -= 1
# if adjacent two pairs overlaps, delete the one overlapped both (update pre)
            pre += 1
            curr += 1
            nxt += 1

        if len(intervals) > 1 and intervals[pre].end > intervals[curr].start : # need remove
            cnt += 1 # must delete one, only difference is updating pre
        return cnt

if __name__ == "__main__":
    intervals = [ [1,2], [2,3], [3,4], [1,3] ]
    intervals = [ [1,6], [2,4], [4,6], [5,7] ]
    intervals = [Interval(1,6), Interval(2,4), Interval(4,6), Interval(5,7)]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
