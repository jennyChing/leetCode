import sys
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: use binary search to find if nums[mid] <= nums[mid + 1]: take right half
        l, r = 0, len(nums) - 1 # r inclusive
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= nums[mid + 1]: # take right half
                l = mid + 1
            else: # take left half
                r = mid # inclusive
        return l
