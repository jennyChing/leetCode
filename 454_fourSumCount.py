'''
454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
# reduce time to O(n^2) with hashtables
        memo = collections.defaultdict(int)
        for a in A:
            for b in B:
                memo[(a + b)] += 1
                print(a + b)
        res = 0
        for c in C:
            for d in D:
                print(-(c + d))
                if -(c + d) in memo:
                    res += memo[-(c + d)]
        return res

    def fourSumCount_revise(self, A, B, C, D):
        cnt = collections.Count([a + b for a in A for b in B])
        return sum(memo[-(c + d)] for c in C for d in D)


if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    res = Solution().fourSumCount(A, B, C, D)
    print(res)
