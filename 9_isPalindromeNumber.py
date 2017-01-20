'''
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = 1
        while x / digits > 10:
            digits *= 10

        while x:
            left, right = x % digits, x % 10
            if left != right:
                return False
            x = (x % digits) // 10
            digits /= 100
        return True

if __name__ == "__main__":
    res = Solution().isPalindrome(10010)
    print(res)
