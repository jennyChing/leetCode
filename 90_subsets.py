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
        if you skip this one, if next one is duplicate one, you cannot choose it
        sort it and while recursing check if the current one is same as the last one, then skip it

        index = i + 1 (index - 1 is the last one you select)
        """


