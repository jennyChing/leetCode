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
        for i in range(len(nums)):
            print(nums[i])
            if i > 0 and nums[1] == nums[i - 1]: # to avoid duplicate
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue # second check
                k, l = j + 1, len(nums) - 1 # need move range to after l
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        res.append((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]: # repeated
                            k += 1 # skip
                        while k < l and nums[l] == nums[l + 1]: # repeated
                            l -= 1 # skip
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
        print(res)
        return [list(r) for r in set(res)]

if __name__ == "__main__":
    nums = [1, 0, 0, -1, 0, -2, 2]
    res = Solution().fourSum(nums, 0)
    print(res)
