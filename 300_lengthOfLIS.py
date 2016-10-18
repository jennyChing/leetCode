'''
binary search

300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return len(nums)
        M = [None] * len(nums)
        P = [None] * len(nums)
        L, M[0] = 1, 0
        for i in range(1, len(nums)):
            lower, upper = 0, L
            #print(nums[M[upper - 1]], nums[i], "L/i :", L, i)
            if nums[M[upper - 1]] < nums[i]:
                #print("smaller then nums[i] :", nums[M[upper - 1]], nums[i])
                j = upper
            else:
                #print("larger  then nums[i] :", nums[M[upper - 1]], nums[i])
                j = upper
                while upper > lower + 1:
                    mid = (upper + lower) // 2
                    #print(lower, mid, upper, j)
                    if nums[M[mid - 1]] < nums[i]:
                        lower = mid
                    else:
                        upper = mid
                j = lower
            #print("to 2nd part i/j :", i, j)
            P[i] = M[j - 1]
            if j == L or nums[i] < nums[M[j]]:
                M[j] = i
                L = max(L, j + 1)
            print(i, L, M, P)
        result = []
        pos = M[L - 1]
        for _ in range(L):
            result.append(nums[pos])
            pos = P[pos]
        return len(result)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [2, 15, 3, 7, 8, 6, 19]
    res = Solution().lengthOfLIS(nums)
    print(res)
