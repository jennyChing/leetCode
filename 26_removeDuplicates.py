'''
26. Remove Duplicates from Sorted Array  QuestionEditorial Solution

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.
'''
class Solution(object):
# modifing the array will change the length of it
    def removeDuplicates(self, nums):
        i = 1
        for j in range(len(nums)):
            if nums[i-1] != nums[j]:
                print(nums[i-1], nums[j], i, j, nums)
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return len(nums[:i])
if __name__ == '__main__':
    nums = [1, 1, 2, 3, 4, 4, 5]
    print(Solution().removeDuplicates(nums))
