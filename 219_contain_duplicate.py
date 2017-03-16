'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_nums = set()
        for i in range(k):
            if nums[i] in dict_nums:
                return True
            dict_nums.add(nums[i])
            print(i, k, dict_nums)

        for i in range(k, len(nums)):
            if nums[i] in dict_nums:
                return True
            dict_nums.add(nums[i])
            print(i, k, dict_nums)
            dict_nums.discard(nums[i - k])
            print(i, k, dict_nums)
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
	# O(n * k) TL => idea: moving window record i ~ k elements in memo to reduce time to O(n + k)
        memo = set()
        for i, n in enumerate(nums):
            if i - k > 0:
                memo.remove(nums[i - k - 1]) # first remove
            if n in memo:
                return True
            memo.add(n) # then add
        return False

if __name__ == '__main__':
    nums = [-2, 0, 1, 2, -1, 4]
    k = 5
    print(Solution().containsNearbyDuplicate(nums, k))

