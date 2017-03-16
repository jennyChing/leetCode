# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # idea: sort by start and compare start with next interval's end, if s2 < e1, merge as s1~max(e1, e2)
        # key: need to merge more then 1! use while loop (if merge, i stays the same)
        intervals = sorted(intervals, key=lambda x: x.start)
        i = 1
        while i < len(intervals):
            if intervals[i].start <= intervals[i - 1].end:
                intervals[i - 1] = Interval(intervals[i - 1].start, max(intervals[i - 1].end, intervals[i].end))
                del intervals[i]
            else:
                i += 1
        return intervals

# faster:
	intervals = sorted(intervals, key=lambda x:x.start)
        res = [] # instead of del, use new array to speed up!
        for i in intervals:
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res

if __name__ == '__main__':
    res = Solution().merge([Interval(1, 4), Interval(4, 5)])
    for i in res:
        print(i.start, i.end)
