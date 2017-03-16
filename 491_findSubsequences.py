'''
491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .
'''
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
# key: duplicated num in nums, if skipped need to skip both
        def dfs(level, partial):
            if len(partial) >= 2:
                res.append(partial)
            memo = set() # each level record number used
            for i in range(level, len(nums)):
                print("iterate:", i, nums[i], "start:", level, memo, partial)
                if nums[i] in memo:
                    print(i, nums[i], level)
                    continue
                memo.add(nums[i])
                if not partial or nums[i] >= partial[-1]: # increasing
                    dfs(i + 1, partial + [nums[i]])
            print("iterate end")
        res = []
        dfs(0, [])
        return res

if __name__ == '__main__':
    res = Solution().findSubsequences([4, 7, 7, 6, 4, 7])
    print(res)


