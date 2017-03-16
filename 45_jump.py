'''
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# idea: for each reachable range, find the position with max jump length
        i = cnt = 0
        last_max_reach = cur_max_reach = 0
        while cur_max_reach < len(nums) - 1:
            while i <= last_max_reach:
                cur_max_reach = max(i + nums[i], cur_max_reach)
                print("curr max:", cur_max_reach, last_max_reach, i, nums[i])
                i += 1
            last_max_reach = cur_max_reach
            cnt += 1
            print(i, cnt)
        return cnt

# Incorrect idea: for each reachable range, find the position with max jump length
        i = cnt = 0
        if len(nums) <= 1:
            return 0
        if nums[i] >= len(nums) - 1:
            return 1
        while i + nums[i] < len(nums) - 1:
            tmp, maxJump = i, 0
            for j in range(1, min(len(nums) - i, nums[i] + 1)):
                if nums[i + j] >= maxJump: # update when = as well! take the last 1 with same nums[i + j]
                    maxJump = nums[i + j]
                    tmp = i + j # idx of current max jump
                    if tmp >= len(nums) - 1:
                        break
            i = tmp
            cnt += 1
        cnt += 1
        return cnt

if __name__ == '__main__':
    nums = [1,1,2,1,1]
    nums = [2,3,1,1,4]
    nums = [3,2,1]
    nums = [10,9,8,7,6,5,4,3,2,1,1,0]
    nums = [3,4,3,2,5,4,3]
    res = Solution().jump(nums)
    print(res)

