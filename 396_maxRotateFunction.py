'''
396. Rotate Function

Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
'''
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
# O(n): first n - 1 elements index all add 1 (result += each element * 1)
     #  last element index - len(A) => become zero
        total = sum(A)
        f_value = 0
        for i, v in enumerate(A):
            f_value += i * v
        max_f = f_value
        for i in range(len(A) - 1, 0, -1):
            f_value += total - (len(A) * A[i]) # (total-A[i] - (len(A)-1)*A[i]
            max_f = max(f_value, max_f)
        return max_f

if __name__ == "__main__":
    A = [4, 3, 2, 6]
    res = Solution().maxRotateFunction(A)
    print(res)
