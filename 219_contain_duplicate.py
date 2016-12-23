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

if __name__ == '__main__':
    nums = [-2, 0, 1, 2, -1, 4]
    k = 5
    print(Solution().containsNearbyDuplicate(nums, k))

