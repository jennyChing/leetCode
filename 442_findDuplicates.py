'''
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
# for loop n in nums and mark A[A[i] - 1] as -1 to see if repeated visit exits
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                res.append(abs(nums[i]))
        return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    res = Solution().findDuplicates(nums)
    print(res)
