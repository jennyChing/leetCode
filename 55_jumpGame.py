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
        print(len(nums))
        if len(nums) == 1:
            return True
        def __directed_dfs(level):
            print(level, len(nums))
            if level >= len(nums):
                return True
            for l in range(nums[level], 0, -1): # all possible jumping that could be reached
                print(l)
                return __directed_dfs(level + l)
            return False

        return __directed_dfs(1)

if __name__ == "__main__":
    nums = [3,2,1,0,4]
    nums = [1, 2]
    res = Solution().canJump(nums)
    print(res)

