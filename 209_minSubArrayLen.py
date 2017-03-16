'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        curr_sum, i, res = 0, 0, float('inf')
        for j in range(len(nums)):
            curr_sum += nums[j]
            print("iterate j :", j)
            while i <= j and curr_sum >= s: # when still valid, try to move pointer i forward
                print(res, curr_sum, i, j)
                res, curr_sum = min(res, j - i + 1), curr_sum - nums[i]
                i += 1
        return res if res < float('inf') else 0

# second attempt
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # idea: 2 pointers i and j -> inside for loop j, while i <= j and sum(nums[i:j]) > s: i++, stop moving i forward when no longer > s (len = j - i + 1, for loop j and return the min_len)
        i, j , min_len, cur_sum = 0, 0, sys.maxint, 0
        while j < len(nums): # j++ when cur_sum < s
            cur_sum += nums[j]
            while i <= j and cur_sum >= s: # start moving i till cur_sum >= s! (stop when cur_sum < s)
                min_len = min(min_len, j - i + 1)
                cur_sum -= nums[i] # i is moved forward so the first element at old i is out of range
                i += 1 # shorten subarray by moving i forward
            j += 1
        return min_len if min_len != sys.maxint else 0

if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    res = Solution().minSubArrayLen(7, nums)
    print(res)
