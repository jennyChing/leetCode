from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            product = reduce( (lambda x, y: x * y), nums[:i] + nums[i + 1:])
            res.append(product)
        return res

