'''
400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        split = [9]
        while split[-1] < n:
            split.append(split[-1] + 9 * 10**len(split) * (len(split) + 1))
        print(split)
        split = [i + 1 for i in split]
        number = (n - split[-2]) // len(split) + 10**(len(split) - 1)
        digit = (n - split[-2]) % len(split)
        print(number, digit)
        return str(number)[digit]

if __name__ == "__main__":
    res = Solution().findNthDigit(1000)
    print(res)
