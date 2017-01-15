'''
473. Matchsticks to Square

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
'''
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def __directed_dfs(nums, idx, target):
            if idx == len(nums): # use up all the matchsticks
                return True
            for i in range(4): # four sides
                if target[i] >= nums[idx]:
                    target[i] -= nums[idx]
                    if __directed_dfs(nums, idx + 1, target): # idx move down by 1 ( same as delete 1 mactchstick in nums)
                        return True
                    target[i] += nums[idx] # not valid, reset and backtrack
            return False
        if len(nums) < 4 or sum(nums) % 4 != 0: return False
        nums.sort(reverse=True)
        target = [sum(nums) // 4] * 4 # use the array to record each side left
        return __directed_dfs(nums, 0, target) # index 0 is the largest value

if __name__ == "__main__":
    nums = [1,1,2,2,2]
    nums = [3,3,3,3,4]
    res = Solution().makesquare(nums)
    print(res)
