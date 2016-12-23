'''
220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''
import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        d = collections.OrderedDict()
        for i in range(len(nums)):
            if nums[i] - t in d and abs(

            if i + 1 > k:
                d.popleft()
        return False

if __name__ == "__main__":
    nums = [2, 2]
    k, t = 3, 0
    res = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print(res)
