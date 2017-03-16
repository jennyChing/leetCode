'''
34. Search for a Range

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        r, l = len(nums) - 1, 0
        hasTarget = False
        while l <= r: # check your bounds!!!
            mid = (l + r) // 2
            if nums[mid] == target:
                hasTarget = True
                # move your l, r is better then moving mid: no need for extra variables
                while nums[l] < target:
                    l += 1
                while nums[r] > target:
                    r -= 1
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [l, r] if hasTarget else [-1, -1]

if __name__ == "__main__":
    t1 = [5, 7, 7, 8, 8, 10]
    res = Solution().searchRange(t1, 8)
    print(res)
