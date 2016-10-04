'''
binary search
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.
'''
class Solution(object):
    def isPerfectSquare(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        right, left = num // 2 + 1, 1
        while right > left + 1:
            mid = (right - left) // 2 + left
            if mid * mid == num:
                return True
            elif mid * mid < num:
                print("search for the larger half :", mid)
                left = mid
            else: # 往小的那半找
                print("search for the smaller  half :", mid)
                right = mid
        return False
if __name__ == '__main__':
    res = Solution().isPerfectSquare(100)
    print(res)
