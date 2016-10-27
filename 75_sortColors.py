'''
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''
class Solution(object):
    def sortColors(self, nums):
        # need 3 pointers for 3 colors!! One starting from the end of the list
        a, b, c = 0, 0, len(nums) - 1
        while b <= c:
            print(nums, a, b, c)
            if nums[a] == 0:
                nums[b], nums[a] = nums[a], nums[b]
                a += 1
                b += 1
            elif nums[b] == 1:
                b += 1
            else:
                nums[b], nums[c] = nums[c], nums[b]
                c -= 1
        return(nums)

if __name__ == "__main__":
    res = Solution().sortColors([0,1,2,0,1,1,2])
    print(res)
