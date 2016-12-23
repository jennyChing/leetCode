'''
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        mask = 1
        while mask <= max(nums):
            mask *= 10
            print(mask)
        nums_mask = []
        for n in nums:
            prefix = n
            while prefix < mask:
                prefix *= 10
            nums_mask += prefix * mask + n,
        nums_mask.sort(reverse=True)
        print(nums_mask)
        res = ""
        for n in nums_mask:
            res += str(n % mask)
        return res

if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    nums = [121, 12]
    res = Solution().largestNumber(nums)
    print(res)
