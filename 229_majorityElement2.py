'''
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return nums

# separate the nums into < pivot, = pivot and > pivot, then check the length of = pivot elements
        def partition(start, end, major):
            # base case: lenght of elements is less then n/3 so not possible
            if end - start < len(nums) // 3:
                return
            left, right, pivot = start, end - 1, nums[end]
            print(left, right)

            for i, v in enumerate(nums[start:right + 1]):
                if v > pivot:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                elif v < pivot:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            if right - left + 1 > len(nums) // 3:
                # append if match criteria:
                major.append(nums[pivot])
            print(nums)
# recursively look at left and right part to find more major elements if any
            partition(start, left - 1, major)
            partition(right + 1, end, major)

        major = []
        partition(0, len(nums) - 1, major)
        return major
if __name__ == "__main__":
    nums = [1, 2, 3]
    nums = [2, 2, 1, 3]
    nums = [1, 0, 1, 3, 1, 5, 1]
    res = Solution().majorityElement(nums)
    print(res)
