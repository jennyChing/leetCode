'''
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, area = [-1], 0 # key: to deal with last height
        heights.append(0) # to deal with last height corner case
        for i, v in enumerate(heights):
            while v < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h * w)
                print(area, "height", h, "width", w, v, i)
            stack.append(i)
        return area

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    heights = [2,1,2]
    res = Solution().largestRectangleArea(heights)
    print(res)

