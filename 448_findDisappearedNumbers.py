'''
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums.sort()
        i = 0
        for n in range(1, len(nums) + 1):
            if (i < len(nums) and n < nums[i]) or (i == len(nums) and n > nums[-1]):
                res.append(n)
            while i < len(nums) and n >= nums[i]:
                i += 1
        return res

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                temp = nums[i]
                nums[i] = -1
                while nums[temp - 1] != temp and temp != -1:
                    nums[temp - 1], temp = temp, nums[temp - 1]

        for j in range(len(nums)):
            if nums[j] == -1:
                result.append(j + 1)
        return result

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            nums[(n - 1) % len(nums)] += len(nums)
            print(n - 1 % len(nums))
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                ans.append(i + 1)
        return ans

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    res = Solution().findDisappearedNumbers(nums)
    print(res)
