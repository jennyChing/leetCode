'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, res = [], 0
        cache = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h: # end if 右邊有比較大的or out of heights
                print("pop", height[stack[-1]], h, cache)
                res += (height[stack[-1]] - cache) * (i - stack[-1] - 1) # index calculate the width
                cache = height[stack[-1]] # record last popped
                stack.pop()
                print("pop", stack, res)
            if stack: # current h is not the highest
                res += (h - cache) * (i - stack[-1] - 1) # index calculate the width
                print(stack, res)
                cache = h # record current highest
            stack.append(i) # record the index not height value
        return res

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = Solution().trap(height)
    print(res)

