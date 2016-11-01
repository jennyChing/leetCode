'''
39. Combination Sum

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
# [key] backtrack when target remains less then zero!

        res = []
        candidates.sort()

        def __directed_combination(start, target_remain, partial, res):

            # Backtracking:
            if target_remain < 0:
                return

            # Step3: Append the valid combination to the result array
            if not target_remain:
                res.append(partial)
                return res

            # Step2: validate and recursive the rest part (each i in the for loop will start a new empty path)
            for i in range(start, len(candidates)):
                __directed_combination(i, target_remain - candidates[i], partial + [candidates[i]], res)
            return res

            # Step1: starting point: start from the first element
        return  __directed_combination(0, target, [], [])

if __name__ == "__main__":
    res = Solution().combinationSum([2, 3, 6, 7], 7)
    print(res)



