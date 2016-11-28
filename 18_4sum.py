'''
18. 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for k in range(len(nums)):
            for l in range(k + 1, len(nums)):
                i, j = 0, k - 1
                while i < j:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        res.append((nums[i], nums[j], nums[k], nums[l]))
                        while i < j and nums[i] == res[-1][0]:
                            i += 1
                        while i < j and nums[j] == res[-1][1]:
                            j -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        i += 1
                    else:
                        j -= 1
        print(res)
        return [list(r) for r in set(res)]


if __name__ == "__main__":
    nums = [1, 0, 0, -1, 0, -2, 2]
    res = Solution().fourSum(nums, 0)
    print(res)
