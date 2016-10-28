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
        most_right = right
        start = 0
        while left <= right:
            mid = (left + right ) // 2
            if most_right > mid and nums[mid] > nums[mid + 1]:
                start = mid + 1
                break
            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        nums = nums[start:] + nums[:start]

        # now it is simple binary search:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                print(mid, start)
                if mid < start: # deal with index problem
                    return mid + start
                return mid + 1 - start
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

if __name__ == '__main__':
    nums = [1, 3]
    nums = [4, 5, 6, 7, 0, 1, 2]
    res = Solution().search(nums, 7)
    print(res)


