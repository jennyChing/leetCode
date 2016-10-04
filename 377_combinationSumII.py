'''
377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Note that different sequences are counted as different combinations. (coin change problems doesn't care about the sequence, counting as same)
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        # base_case: target is 0 then only 1 way (all zeros)
        if target == 0:
            return 1
        cnt = 0
        # for rest of the case, we can either include the num or exclude
        # coin change solution (different sequence count as same combination)
        # def _get_comb_matrix(nums, r):
        #     m = [[0 for _ in range(r + 1)] for _ in range(len(nums) + 1)]
        #     for i in range(len(nums) + 1):
        #         m[i][0] = 1
        #     return m
        # m = _get_comb_matrix(nums, target)

        # for n in range(1, len(nums) + 1):
        #     for t in range(1, target + 1):
        #         if nums[n - 1] <= t:
        #             # reduce the amount by n and use the subproblem result (target - nums[n]
        #             # then also add the value from the upper row
        #             m[n][t] = m[n - 1][t] + m[n][t - nums[n - 1]]
        #             print("num <= target: ", nums[n - 1], t, m)
        #         else: # copy the value from the upper row
        #             m[n][t] = m[n - 1][t];
        #             print("num > target :", nums[n - 1], t, m)
        nums, m = sorted(nums), [1] + [0] * target # base case: 1 way
        for i in range(target + 1):
            for n in nums:
                if n > i:
                    break
                elif n == i:
                    m[i] += 1
                    print(m, n, i)
                else:
                    m[i] += m[i - n]
                    print(m, n, i, i - n)
        return m[target]

if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 5
    res = Solution().combinationSum4(nums, target)
    print(res)



