'''
Kadane algorithm
'''
class Solution(object):
    def maxSubArray(self, nums):
        max_so_far, max_end_here, less_neg = 0, 0, float('-inf')
        isAllNeg = True
        for n in nums:
            max_end_here += n
            #print(less_neg)
            if n <= 0:
                less_neg = max(less_neg, n)
            if max_end_here < 0:
                max_end_here = 0
            if max_end_here > max_so_far: # update max_so_far
                isAllNeg = False
                #print(n, max_end_here, max_so_far)
                max_so_far = max_end_here
        if isAllNeg == True:
            return less_neg
        return max_so_far
# second attempt:
import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: 1 dimension dp table, initial is [from i to j in range(len(nums))], then each iteration minus the first element O(n^2) -> reduce to O(n) using
        if len(nums) == 1:
            return nums[0]
        dp = [0]
        for n in nums:
            dp.append(n + dp[-1])
        dp = dp[1:]
        max_sum = max(dp)
        for i, n in enumerate(nums[:-1]):
            dp = [s - n for s in dp]
            max_sum = max(max_sum, max(dp[i + 1:]))
        return max_sum

# Google solution
import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: 1 dimension dp table, initial is [from i to j in range(len(nums))], then each iteration minus the first element O(n^2) -> reduce to O(n) using cur_sum and max_sum variable
        cur_sum = max_sum = nums[0]
        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n) # continue with n or restart from n
            max_sum = max(cur_sum, max_sum)
        return max_sum

if __name__ == '__main__':
    nums = [-2]
    res = Solution().maxSubArray(nums)
    print(res)


