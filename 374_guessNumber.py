'''
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.

Binary search
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guess(self, num):
        return 0 if num == 6 else -1 if num > 6 else 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        first narrow to a range with x2 or /2, then start +1 or -1
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if Solution().guess(mid) == -1:
                right = mid - 1 # new range not including mid anymore
            elif Solution().guess(mid) == 1:
                left = mid + 1 # new range not including mid anymore
            else:
                return mid
if __name__ == '__main__':
    res = Solution().guessNumber(10)
    print(res)


