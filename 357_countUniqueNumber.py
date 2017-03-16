class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
# attempt 4
        if n == 1:
            return 10
        base, accu_sum = 1, 0
        for i in range(n):
            base *= (10 - i)
            recurr = 1
            for j in range(1, i):
                recurr *= (10 - j)
            print("rec :", recurr, recurr * (i))
            accu_sum += (i) * recurr
            print(base)
            print(accu_sum)
        return base + accu_sum
# attempt 3 (Discuss: 遞迴公式)
        #n = min(n, 9)
        #last, cache, prod = 0, 0, 1
        #for index in range(1, n):
        #    cache = index * prod
        #    print(cache, index, prod)
        #    print("cacheing: ", last, cache, prod, index)
        #    cache += last
        #    print(cache)
        #    print("update cache: ", last, cache, prod, index)
        #    last = cache
        #    prod *= (10 - index)
        #    print("update prod :", last, cache, prod, index)
        #return (10 * prod + cache) if n > 0 else 1
# attempt 2
        #uni = res = 1
        #for i in range(n):
        #    uni *= 9 if i == 0 else (10 - i)
        #    res += uni
        #return res
# attempt 1
        #digits = 1
        #if n > 10:
        #   uni = 9
        #else:
        #    return n
        #while n // 10:
        #    uni *= (9 - digits + 1)
        #    digits += 1
        #    n //= 10
        #return uni
if __name__ == '__main__':
    res = Solution().countNumbersWithUniqueDigits(4)
    print(res)
