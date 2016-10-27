'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

[Solutions]
Two pointers, one from start and one from the back narrowing down the width of the container by comparing heights

1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
2. All other containers are less wide and thus would need a higher water level in order to hold more water.
3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left, right = 0, len(height) - 1
        while left < right:
            water = max(water, (right - left) * min(height[left], height[right])) # calculate the area for current left & right
            # take the one with more potential! the higher height one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water
if __name__ == "__main__":
    res = Solution().maxArea([1, 4, 5, 3])
    print(res)
