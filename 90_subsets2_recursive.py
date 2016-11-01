'''
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        index = i + 1 (index - 1 is the last one you select)
        """
        # [Idea:] if you skip this one, if next one is duplicate one, you cannot choose it. So sort it and while recursing check if the current one is same as the last one, then skip it

        res = []
        # sort it to better check the duplication
        nums = sorted(nums)
        def __directed_dfs(res, level, path):
            # complete a path whenever recursive is called
            res.append(path)

            # start for loop from new level
            for i in range(level, len(nums)):
                print(level, i, nums[level])
            # [Special case to handle:] if the next one is a duplicated value and previous wan't selected: cannot select it! (must skip case)
                if i > level and nums[i] == nums[i - 1]: # i > level: skipped
                    continue # need to skip this duplicate value as well
                __directed_dfs(res, i + 1, path + [nums[i]]) # new level is (i + 1) not (level + 1)!

        __directed_dfs(res, 0, [])
        return res
if __name__ == '__main__':
    nums = [1, 2, 2]
    res = Solution().subsetsWithDup(nums)
    print(res)



