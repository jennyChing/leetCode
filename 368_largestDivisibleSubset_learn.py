'''
368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = {-1: set()}
        for x in sorted(nums):
            s[x] = max((s[d] for d in s if x % d == 0), key=len) | {x}
        return list(max(s.values(), key = len))
if __name__ == '__main__':
    nums = [1, 2, 4, 8, 16]
    nums = [1, 2, 3]
    res = sorted(Solution().largestDivisibleSubset(nums))
    print(res)
