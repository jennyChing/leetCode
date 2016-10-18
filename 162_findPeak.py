class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       curr = float('-inf')
       for i in range(len(nums)):
           if nums[i] < curr:
               return i - 1
