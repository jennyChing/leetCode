'''
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==None or nums==[] or nums[0]==0 and len(nums)>1:
            return False
        if len(nums) == 1:
            return True
        curr = nums[0]
        for jump in range(len(nums)):
            # ask: how to know that every step in nums can be reached?
            if curr >= len(nums) - 1:
                return True
            if jump <= curr:
                curr = max(curr, jump + nums[jump])
        return False

if __name__ == "__main__":
    nums = [1, 2]
    nums = [3,2,1,0,4]
    res = Solution().canJump(nums)
    print(res)

