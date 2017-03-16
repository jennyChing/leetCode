'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
import itertools

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
# Using itertools API:
        def __directed_combination(n, k):
            iterable = range(1, n + 1)
            for comb in itertools.combinations(iterable, k):
                yield list(comb)
        return list(__directed_combination(n, k))

# Using generator:
        #def __directed_combination(n, k):
        #    cnt, ans = 0, []
        #    while cnt < n:
        #        while _ in k:
        #            yield cnt

    def combine_dfs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # idea: dfs backtricking solution (too slow...)
        def dfs(partial):
            print(len(partial))
            if len(partial) == k:
                res.append(partial) # main checking condition
                return
            if len(partial) > k:
                return
            # if not valid partial
            for n in nums:
                if n in partial or (partial and n > partial[-1]):
                    continue # already in the partial list
                dfs(partial + [n]) # generate new dfs

        res = []
        nums = [i for i in range(1, n + 1)]
        dfs([])
        return res

if __name__ == "__main__":
    res = Solution().combine_dfs(4, 2)
    print(res)




