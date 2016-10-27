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
if __name__ == "__main__":
    res = Solution().combine(4, 2)
    print(res)




