'''
365. Water and Jug Problem

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
'''
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == z or y == z:
            return True
        def __directed_dfs(res, memo):
            if res == z:
                return True
            if res in memo:
                return
            minus_y = abs(res - y)
            if minus_y > 0:
                return __directed_dfs(minus_y, memo)
            minus_x = abs(res - x)
            if minus_x > 0:
                return __directed_dfs(minus_x, memo)
            sum_two = res + x
            if sum_two < y:
                return __directed_dfs(sum_two, memo)
        if x > y: # make x the smaller jug and y the bigger one
            x, y = y, x
        memo = set()
        res = y - x




if __name__ == "__main__":
    res = Solution().canMeasureWater(3, 5, 4)
    print(res)
