'''
324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''
import statistics
class Solution(object):
    def wiggleSort(self, nums):
        if len(nums) % 2:
            m = sorted(nums)[len(nums)//2]
        else:
            m = (sorted(nums)[len(nums)//2] + sorted(nums)[len(nums)//2 - 1]) / 2
        small, equal, big = [], [], []
        for n in nums:
            if n == m:
                equal.append(n)
            elif n < m:
                small.append(n)
            else:
                big.append(n)
        even, odd = len(nums) - 1 if len(nums) % 2 else len(nums) - 2, len(nums) - 2 if len(nums) % 2 else len(nums) - 1
        wig = [0 for _ in range(len(nums))]
        for n in small:
            wig[even] = n
            even -= 2
        for n in equal:
            if even < 0:
                wig[odd] = n
                odd -= 2
            else:
                wig[even] = n
                even -= 2
        for n in big:
            wig[odd] = n
            odd -= 2
        nums[:] = wig

if __name__ == "__main__":
    nums = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(nums)
    print(nums)
