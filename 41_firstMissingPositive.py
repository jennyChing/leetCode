'''
41. First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
# idea: use array with size of n to record if i in range(1, n + 1) exists, ex: [4, 3, 1, -1] => [T, F, T, T] = 2 does't exist
        idx = 0
        nums = list(set(nums)) # has to be unique!!
# Step1: swap the value if nums[idx] != idx + 1, till meet or out of range
        while idx < len(nums):
            while nums[idx] != idx + 1 and 0 < nums[idx] <= len(nums):
                tmp = nums[idx]
                nums[idx] = nums[nums[idx] - 1]
                nums[tmp - 1] = tmp
            idx += 1
# Step2: find the first missing positive number (i + 1) != n
        for i, n in enumerate(nums):
            if i + 1 != n :
                return i + 1
        return len(nums) + 1
if __name__ == '__main__':
    nums = [3,4,-1,1]
    res = Solution().firstMissingPositive(nums)
    print(res)

