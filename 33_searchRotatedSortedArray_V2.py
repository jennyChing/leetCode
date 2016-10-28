'''
33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def search(self, nums, target):
        # find the start of rotated array
        left, right = 0, len(nums) - 1
        while left + 1 < right: # careful off-by-1 case!!
            mid = (left + right ) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= target < nums[mid]:
                right = mid
            elif nums[mid] <= target <= nums[right]:
                left = mid
            elif nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1


if __name__ == '__main__':
    nums = [4, 4, 5, 6, 7, 0, 1, 2]
    nums = [1, 1, 3, 1]
    res = Solution().search(nums, 3)
    print(res)


