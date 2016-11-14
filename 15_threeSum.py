'''
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        pairs = set()
        for k in range(len(nums)):
            i, j = 0, k - 1
            while i < j:
                print(nums[i] , nums[j] , nums[k])
                if nums[i] + nums[j] + nums[k] == 0:
                    pairs.add((nums[i], nums[j], nums[k]))
                    i += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    j -= 1
        pairs = list(pairs)
        res = []
        for p in pairs:
            res.append(list(p))
        return res

if __name__ == "__main__":
    s = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(s)
    print(res)
