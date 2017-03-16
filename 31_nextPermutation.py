'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
# KEY: move the bigger ones forward to form the lexicographical order (i < j)

# Step1: locate the most right digit i - 1 as start of an ascending order
        while nums[i] <= nums[i - 1] and i > 0: # compare the neighbors
            i -= 1

# Step2: find the right most digit j greater than nums[i - 1] and sort right part starting i
        if i > 0:
        #  Start with j as the new start and sort the right part after i - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # reverse the right part after (start from j + 1) index j to initialize
        nums[i:] = sorted(nums[i:])
        return nums

if __name__ == "__main__":
    nums = [2, 1, 3]
    nums = [2, 3, 1]
    nums = [1,2,3,5,4]
    res = Solution().nextPermutation(nums)
    print(res)
