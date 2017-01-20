'''
462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# If we increase k, the elements <= k will need move one step more, and the elements > k will need to move one step less.
# If there are more elements > k than elements <= k, we should increase k to minimize the moves.
# So we just increase k, until k reach the median of of the nums array. By then, the number of elements <= k equals to that of elements > k.

        if len(nums) < 2: return nums
        median = sorted(nums)[len(nums)//2]
        return sum([abs(median - n) for n in nums])

if __name__ == "__main__":
    nums = [1,2,3]
    nums = [1,0,0,8,6]
    res = Solution().minMoves2(nums)
    print(res)
