'''
binary search

300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return len(nums)
        memo = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    print(memo)
                    memo[i] = max(memo[i], memo[j] + 1)
        return max(memo)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [2, 15, 3, 7, 8, 6, 19]
    res = Solution().lengthOfLIS(nums)
    print(res)
