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
        O(n square) solution:
        """
        memo = [[i] for i in nums]
        # first double for loop record all the numbers larger than nums[i]
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > curr:
                    memo[i].append(nums[j])
                    curr = nums[j]
        # second double for loop start from the back and add any numbers smaller than nums[i]
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < memo[i][0]:
                    memo[i].insert(0, nums[j])
        print(max(memo, key = len))
        max_len = max(memo, key = len)
        return len(max_len)
if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 4]
    nums = [2,15,3,7,8,6,18]
    res = Solution().lengthOfLIS(nums)
    print(res)
