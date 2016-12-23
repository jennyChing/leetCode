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
            bucket = nums[i] // (t + 1)
            print(t + 1, bucket, d, nums[i])
            for key in [bucket - 1, bucket, bucket + 1]: # check nearby values
                print("keys:", key)
                if key in d and abs(d[key] - nums[i]) <= t: # check difference <= t
                    return True
            d[bucket] = nums[i] # cover old bucket value
            if i + 1 > k: # out of range k
                d.popitem(last=False)
        return False

if __name__ == "__main__":
    nums = [2, 4, 6, 9, 2]
    k, t = 3, 1
    res = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print(res)
