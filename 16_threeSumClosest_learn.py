'''
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        final = []
# use triple for loop to list all combinations
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for m in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[m]
                    final.append(total)
        spread = abs(max(final))

# initialize res based on target - max(final) to minimize the spread
        res = min(final) if target - max(final) < 0 else max(final)
        print(spread, final, res)
        for k in final:
            if abs(k - target) <= spread:
                res = k
                spread = abs(k - target)
        return res


if __name__ == "__main__":
    t1 = [0, 0, 0]
    t1 = [-1, 2, 1, 4]
    res = Solution().threeSumClosest(t1, -100)
    print(res)
