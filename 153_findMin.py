'''
binary search
153. Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

Find the minimum element.
'''
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        n = right
        while left <= right:
            mid = (right - left) // 2 + left
            print(mid, n, nums[mid], nums[mid + 1])
            if n > mid and nums[mid] > nums[mid + 1]: # key point: nums[mid] > nums[mid + 1]
                return nums[mid + 1]
            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[0]
if __name__ == '__main__':
    nums = [4, 5, 6, 7, 1, 2]
    res = Solution().findMin(nums)
    print(res)
