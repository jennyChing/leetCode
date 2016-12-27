'''
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
from functools import cmp_to_key
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def custom_cmp(a, b):
            return -1 if int(a + b) > int(b + a) else 1

        nums = sorted([str(x) for x in nums], key=cmp_to_key(custom_cmp))
        return ''.join(str(n) for n in nums).lstrip('0') or '0'

if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    nums = [121, 12]
    res = Solution().largestNumber(nums)
    print(res)
