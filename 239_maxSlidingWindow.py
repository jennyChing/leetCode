'''
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3 [3 -1]
 1 [3  -1  -3] 5  3  6  7       3 [3 -1 -3]
 1  3 [-1  -3  5] 3  6  7       5 [-1, 5]
 1  3  -1 [-3  5  3] 6  7       5 [5, 3]
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
'''
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
# idea: use a stack to record index within k and pop if out of k or v <= stack[-1] -> not possible to be maximun in the following window
        stack, res = collections.deque([]), []
        for i, v in enumerate(nums):
            while stack and i - stack[0] >= k: # first check if out of range
                stack.popleft()
            while stack and v > nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            if i + 1 >= k:
                res.append(nums[stack[0]])
        return res

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    res = Solution().maxSlidingWindow(nums, 3)
    print(res)

