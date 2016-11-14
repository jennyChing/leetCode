'''
386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mask

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
# implement the customized compare and use it as a variable for sorting:
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
    n = 100
    res = Solution().lexicalOrder(n)
    print(res)
