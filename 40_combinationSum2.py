'''
40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
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

            # Special case that needs check (refer to #90, silimilar concept)
                if i != start and candidates[i] == candidates[i - 1]:
                    continue

                __directed_combination(i + 1, target_remain - candidates[i], partial + [candidates[i]], res)
            return res

            # Step1: starting point: start from the first element
        return  __directed_combination(0, target, [], [])

if __name__ == "__main__":
    res = Solution().combinationSum2([2, 3, 6, 7 ,1, 2, 4], 5)
    print(res)


