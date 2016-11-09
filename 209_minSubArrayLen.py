'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        curr_sum, i, res = 0, 0, float('inf')
        for j in range(len(nums)):
            curr_sum += nums[j]
            print("iterate j :", j)
            while i <= j and curr_sum >= s: # when still valid, try to move pointer i forward
                print(res, curr_sum, i, j)
                res, curr_sum = min(res, j - i + 1), curr_sum - nums[i]
                i += 1
        return res if res < float('inf') else 0


if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    res = Solution().minSubArrayLen(7, nums)
    print(res)
