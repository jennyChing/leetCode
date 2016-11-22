'''
50. Pow(x, n)

Implement pow(x, n).
'''
class recursiveSolution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print(x, n, n % 2)
        if not n:
            return 1
        if n < 0: # nagative n will be 倒數
            return 1 / self.myPow(x, -n)
        if n % 2: # need to multiple by n times in the end
            return x * self.myPow(x, n - 1) # already multiple once so take 1 away from n
        # when n % 2 == 0: recurse input with x square and n / 2
        return self.myPow(x * x, n // 2)


class iterativeSolution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
if __name__ == "__main__":
        res = recursiveSolution().myPow(4, 3)
        res = iterativeSolution().myPow(4, 3)
        print(res)
