class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # idea: use (target - n) as key, index of n as value
        memo = {}
        for i, v in enumerate(nums):
            if v in memo:
                print([i] + [memo[v]])
                return [memo[v]] + [i]
            memo[target - v] = i
