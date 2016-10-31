'''
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # could use recursive/bitwise/DP
        res = []
        def __directed_chose(res, level, partial):
            # base case:
            if level == len(nums):
                res.append(partial)
                return
        # case not choose nums[level]:
            __directed_chose(res, level + 1, partial)
        # case choose nums[level]:
            __directed_chose(res, level + 1, partial + [nums[level]])
        __directed_chose(res, 0, [])
        return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().subsets(nums)
    print(res)



