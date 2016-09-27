class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for d, n in zip(dict, nums):
            result += d * (num // n)
            num %= n
            print(num, result)
        return result
if __name__ == '__main__':
    res = Solution().intToRoman(2222)
    print(res)

