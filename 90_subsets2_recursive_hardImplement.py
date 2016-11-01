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
        nums = sorted(nums) # sort it to better check the duplication
        def __directed_select(res, level, path, last_skip, isSkip):
            if level == len(nums):
                res.append(path)
                return
            temp = last_skip
            last_skip = nums[level]
            __directed_select(res, level + 1, path, last_skip, True)
# [Special case to handle:] if the next one is a duplicated value and previous wan't selected: cannot select it! (must skip case)
            if isSkip == True and last_skip == nums[level]:
                print("garded", isSkip, nums[level], last_skip)
                __directed_select(res, level + 1, path, last_skip, True)
            else:
                last_skip = temp
                print("not g", isSkip, nums[level], last_skip)
                __directed_select(res, level + 1, path + [nums[level]], last_skip, False)
        __directed_select(res, 0, [], None, False)
        return res
if __name__ == '__main__':
    nums = [1, 2, 2]
    res = Solution().subsetsWithDup(nums)
    print(res)



