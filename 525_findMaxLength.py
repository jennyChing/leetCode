'''
525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
'''
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# idea: prefix sum record sum of 0 to index j, and check in memo if 0 to i exist nums[j] - nums[i - 1] == k
        prefixSum = []
        for i in range(len(nums)):
            nums[i] = 1 if nums[i] == 1 else -1
            if i == 0:
                prefixSum.append(nums[i])
            else:
                prefixSum.append(nums[i] + prefixSum[-1])
        memo, maxL = {0:0}, 0
        for i, p in enumerate(prefixSum):
            print(memo)
            if p in memo:
                maxL = max(maxL, i - memo[p] + 1)
            else:
                memo[p] = i + 1 #
        return maxL

if __name__ == '__main__':
    nums = [0,1,0]
    nums = [0,1,0,0,0,0,1,1,1,1,1]
    res = Solution().findMaxLength(nums)
    print(res)

