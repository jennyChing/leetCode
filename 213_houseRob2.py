'''
213. House Robber2

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def __directed_rangeRob(start, end):
            prev_one, prev_two = 0, 0
            for i in range(start, end):
                curr = max(prev_one, prev_two + nums[i])
                prev_two, prev_one = prev_one, curr
            return prev_one

        if nums == []:
            return 0
        if len(nums) < 2:
            return max(nums)

        # key do 2 times, one starting from index 0 and one from index 1
        return max(__directed_rangeRob(0, len(nums) - 1), __directed_rangeRob(1, len(nums)))


if __name__ == '__main__':
    nums = [1, 0, 1, 2, 1, 4]
    res = Solution().rob(nums)
    print(res)
    assert res == 6
