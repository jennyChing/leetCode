'''
494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def dfs(level, target, partial, max_positive):
            if level == len(nums):
                return 1 if target == 0 else 0
            if target > max_positive or target < -1 * max_positive:
                return 0
            if (level, target) in memo:
                return memo[(level, target)]
            res = dfs(level + 1, target - nums[level], partial + [nums[level]], max_positive - nums[level]) + dfs(level + 1, target + nums[level], partial + [-nums[level]], max_positive - nums[level])
            memo[(level, target)] = res
            return res
        memo = {} # cache intermidiate results
        max_positive = sum(nums)
        return dfs(0, S, [], max_positive)

if __name__ == '__main__':
    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    res = Solution().findTargetSumWays(nums, 0)
    print(res)

