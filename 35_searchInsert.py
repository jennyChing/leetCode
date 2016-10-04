'''
35. Search Insert Position

Binary search

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''
class Solution(object):
    def searchInsert(self, nums, n):
        left, right = 0, len(nums)
        while right > left:
            mid = (right - left) // 2 + left
            if n == nums[mid]:
                return mid
            elif n > nums[mid]:
                left = mid + 1
            else:
                right = mid
        if n < nums[mid]:
            return mid
        return mid + 1
if __name__ == '__main__':
    nums, target = [1], 0
    res = Solution().searchInsert(nums, target)
    print(res)
