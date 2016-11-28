'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums) # use 梯形公式！

        #sort_list = [x for x in range(len(nums) + 1)]
        #print(sort_list)
        #for n in nums:
        #    sort_list.remove(n)
        #return sort_list[0]
if __name__ ==  '__main__':
    res = Solution().missingNumber([0, 3, 2])
    print(res)
