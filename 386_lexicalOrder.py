'''
386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''
from functools import cmp_to_key

class maskSolution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mask = 1
        while mask <= n:
            mask *= 10
            print(mask)
        nums_mask = []
        for i in range(1, n + 1):
            prefix = i
            while prefix < mask:
                prefix *= 10
            nums_mask += prefix * mask + i,
            print(prefix, mask, prefix * mask + i)
        nums_mask.sort()
        print(nums_mask)
        return [num % mask for num in nums_mask]


class Solution(object):
# implement the customized compare and use it as a variable for sorting:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        top = 1
        while top * 10 <= n:
            top *= 10
        top = 100

        def custom_compare(a, b, top=top): # top is an extra variable that need given
            # make a & b to the same length of digits:
            while a < top: a *= 10
            while b < top: b *= 10
            return -1 if a < b else b < a

        return sorted([i for i in range(1, n + 1)], key=cmp_to_key(custom_compare))

if __name__ == '__main__':
    n = 21
    res = maskSolution().lexicalOrder(n)
    print(res)
