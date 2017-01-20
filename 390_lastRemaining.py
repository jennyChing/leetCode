'''
390. Elimination Game

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
'''
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [num for num in range(1, n + 1) if not num % 2]
        isFront = False
        while len(arr) > 1:
            if isFront == True: # delete from the start
                arr = [arr[i] for i in range(len(arr)) if i % 2] # left with idx1, 3, 5.... elements
                print(arr)
                isFront = False # next delete from the back
            else: # delete from the back
                if len(arr) % 2:
                    arr = [arr[i] for i in range(len(arr)) if i % 2] # left with idx1, 3, 5.... elements
                    print(arr)
                else:
                    arr = [arr[i] for i in range(len(arr)) if not i % 2] # left with idx0, 2, 4.... elements
                    print(arr)
                isFront = True # next delete from the front
        return arr[0]

    def lastRemaining_refer(self, n):
        start = size = inv = 1
        while n > 1:
            start = start + inv * size + 2 * (n // 2 - 1) * inv * size
            size *= 2
            inv *= -1
            n //= 2
            print(start, size, inv, n)
        return start

if __name__ == "__main__":
    res = Solution().lastRemaining_refer(100)
    print(res)

