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
        if len(nums) < 2:
            return nums
        nums.sort()
        divide_dict = {n: set([n]) for n in nums} # every element's base case: dividiable by itself
        for n in nums:
            max_d = []
            for d in divide_dict:
                if n % d == 0 and len(divide_dict[d]) + 1 >= len(max_d):
                    max_d = list(divide_dict[d]) # copy the longest subset and caseful not to modify divide_dict[d]
                    if max_d[-1] != n:
                        max_d.append(n) # append itself to the list
                    divide_dict[n] = set(max_d) # replace with longer list
        return sorted(list(max(divide_dict.values(), key = len)))

if __name__ == '__main__':
    nums = [1, 2, 4, 8, 16]
    nums = [1, 2, 3]
    res = sorted(Solution().largestDivisibleSubset(nums))
    print(res)
