class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead. (cannot copy large portion of the array)
        """
        if k != 0:
            new_start = len(nums) - k
            print(new_start)
            nums[:] = nums[new_start:] + nums[:new_start] # [:] means in place modify!
            print(nums)
if __name__ == '__main__':
    Solution().rotate([1,2,3,4,5,6,7], 3)
