'''
496. Next Greater Element I

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        maxE = max(nums)
        stack = []
        nextG = {}
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == maxE:
                nextG[nums[i]] = -1
            elif stack and nums[i] <= stack[-1]:
                nextG[nums[i]] = stack[-1]
            else:
                while stack and nums[i] > stack[-1]:
                    stack.pop()
                nextE = stack[-1] if stack else -1
                nextG[nums[i]] = nextE
            stack.append(nums[i])
        res = []
        for n in findNums:
            res.append(nextG[n])
        return res

if __name__ == '__main__':
    findNums, nums = [4,1,2], [1,3,4,2]
    res = Solution().nextGreaterElement(findNums, nums)
    print(res)

