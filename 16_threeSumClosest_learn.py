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
        nums.sort()
        spread = float('inf')
        for k in range(1, len(nums)):
            i, j = 0, k - 1
            while i < j: # use pointer i & j in for loop through k
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == target:
                    return target
                elif abs(sum3 - target) < spread:
                    res = sum3
                    spread = abs(sum3 - target)
                if target - sum3 > 0:
                    i += 1
                else:
                    j -= 1
        return res

if __name__ == "__main__":
    t1 = [0, 0, 0]
    t1 = [0,2,1,-3]
    res = Solution().threeSumClosest(t1, 1)
    print(res)
