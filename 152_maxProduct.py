'''
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos, neg = [nums[0]] + [1] * (len(nums) - 1), [nums[0]] + [1] * (len(nums) - 1)
        for i in range(1, len(nums)):
            tup = (nums[i] * pos[i - 1], nums[i] * neg[i - 1], nums[i])
            pos[i], neg[i] = max(tup), min(tup)
        return max(pos)

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    res = Solution().maxProduct(nums)
    print(res)
