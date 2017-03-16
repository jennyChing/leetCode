class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n)
        cnt = 0
        print(bin_n, n)
        for b in bin_n:
            print(b)
            if b == '1':
               cnt += 1
        return cnt

	return bin(n).count('1')

