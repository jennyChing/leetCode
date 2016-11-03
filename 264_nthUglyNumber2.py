'''
264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

1. The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
3. The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = {1:1}
        p2 = p3= p5 = 1 # use p2/3/5 to record the accumalated times of the number so far
        for i in range(2, n + 1):
            # find the next smallest ugly number:
            while N[p2] * 2 <= N[i - 1]: # if can multiple more one 2 and stay less then the last number
                p2 += 1
            while N[p3] * 3 <= N[i - 1]: # if can multiple more one 2 and stay less then the last number
                p3 += 1
            while N[p5] * 5 <= N[i - 1]: # if can multiple more one 2 and stay less then the last number
                p5 += 1
            N[i] = min(N[p3] * 3, min(N[p2] * 2, N[p5] * 5))
        return N[n]


if __name__ == '__main__':
    res = Solution().nthUglyNumber(13)
    print(res)

