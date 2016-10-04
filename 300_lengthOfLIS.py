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
        print(M, P)
        for i in range(1, len(nums)):
            lower, upper = 0, L
            if nums[M[upper - 1]] < nums[i]:
                j = upper
            else:
                while upper > lower + 1:
                    mid = (upper + lower) // 2
                    if nums[M[mid - 1]] < nums[i]:
                        lower = mid
                    else:
                        upper = mid
                j = lower
            P[i] = M[j - 1]
            print(i, nums[i], M, P)
            if j == L or nums[i] < nums[M[j]]:
                M[j] = i
                L = max(L, j + 1)
        result = []
        pos = M[L - 1]
        for _ in range(L):
            result.append(nums[pos])
            pos = P[pos]
        return len(result)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = Solution().lengthOfLIS(nums)
    print(res)
