'''
313. Super Ugly Number

Ugly numbers are positive numbers whose prime factors only include the given primes list.

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
'''
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        return the nth ugly number.
        """
# TL solution:
        N = {1:1}
        cnt = [1 for _ in primes]
        for i in range(2, n + 1):
            min_next = float('inf')
            for j in range(len(primes)):
                while N[cnt[j]] * primes[j] <= N[i - 1]:
                    cnt[j] += 1
                    print(cnt)
                min_next = min(N[cnt[j]] * primes[j], min_next)
            N[i] = min_next
        return N[n]

# reference solution:
        #res, cnt = [1], [0] * len(primes)
        #for _ in range(n - 1):
        #    res.append(min(res[idx] * p for idx, p in zip(cnt, primes)))
        #    #print(res)
        #    for i, idx in enumerate(cnt):
        #        if res[idx] * primes[i] == res[-1]:
        #            print(res[idx], primes[i], res[-1], i, idx, res, cnt)
        #            cnt[i] += 1
        #return res[-1]

if __name__ == '__main__':
    res = Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
    print(res)
