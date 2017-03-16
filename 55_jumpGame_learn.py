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

# second attempt
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # idea: 1D array record first i elements can reach target index i O(n) => TL, go from start or backwards O(n)

# sol1: from start record max reachable index
        max_reachable = 0
        for i, v in enumerate(nums):
            if i > max_reachable: return False # cannot reach index i
            max_reachable = max(max_reachable, i + v)
        return max_reachable >= len(nums) - 1


# sol2: from back record max reachable index
        backward_traverse = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= backward_traverse:
                backward_traverse = i # backward_traverse can reach index i
        return not backward_traverse # meet index 0 from the back or not


# sol3: 1D array slow O(n)
        dp = [True] + [False for _ in range(len(nums) - 1)] #  initially positioned at the first index
        for i in range(len(nums)): # record reachable by first i elements
            if dp[i] == False:
                continue
            for j in range(1, 1 + nums[i]): # only update dp array when nums[i] is True
                if i + j + 1 >= len(nums): # can reach last index from nums[i]
                    return True
                dp[i + j] = True
        return dp[-1]

if __name__ == "__main__":
    nums = [1, 2]
    nums = [3,2,1,0,4]
    res = Solution().canJump(nums)
    print(res)

