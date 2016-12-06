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
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = statistics.median(map(float, nums))
        wig = [0 for _ in range(len(nums))]
        odd = 1
        even_front, even_back = 0, len(nums) - 1
        isFilledEven = True # start filling the same num from the beginning of odd index
        for n in nums:
            print(n, wig, even_back, even_front, odd)
            if n == m:
                print(isFilledEven)
                if isFilledEven == True:
                    wig[odd] = n
                    odd += 2
                    isFilledEven = False
                else:
                    wig[even_back] = n
                    even_back -= 2
                    isFilledEven = True
            elif n < m:
                wig[even_front] = n
                even_front += 2
            elif n > m:
                wig[odd] = n
                odd += 2
        return wig


if __name__ == "__main__":
    nums = [1, 5, 1, 1, 6, 4]
    nums = [1, 3, 2, 2, 3, 1]
    res = Solution().wiggleSort(nums)
    print(res)
