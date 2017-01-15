'''
416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2 or sum(nums) % 2: return False
        nums.sort()
        dp = [[0] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, sum(nums) // 2 + 1):
# check if first i elements can form target value j (lookup relationship)
                if nums[i - 1] == j:
                    dp[i][j] = 1
                    continue
                if j - nums[i - 1] > -1:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return True if sum(dp[i][-1] for i in range(len(nums) + 1)) > 0 else False

    def canPartition_refer(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2 or sum(nums) % 2: return False
        nums.sort()
        dp = [False] * (sum(nums) // 2 + 1)
        for i in range(1, len(nums) + 1):
            for j in range(sum(nums) // 2, 0, -1): # fill array from the back
                if nums[i - 1] == j:
                    dp[j] = True
                    continue
                dp[j] = dp[j] or (j >= nums[i - 1] and dp[j - nums[i - 1]])
        return dp[-1]

if __name__ == "__main__":
    nums = [1, 2, 3, 5]
    nums = [1, 5, 11, 5]
    nums = [1,2,3,4,5,6,7]
    nums = [2,2,3,5]
    res = Solution().canPartition_refer(nums)
    print(res)
