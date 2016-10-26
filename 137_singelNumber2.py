'''
137. Single Number II

Given an array of integers, every element appears three times except for one. Find that single one.
'''
class Solution(object):
    def singleNumber(self, nums):
# convert negative numbers (bit complementary)
        def __convert(x):
            return x if x < 2**31 else x - 2**32

        # use 32 constants to count each bit and mod it by 3 (the single number could not be mod by 3)
        table = [0] * 32
        for n in nums:
            for i in range(32):
                # cnt the corresponding bits of nums
                table[i] += n & 1
                n >>= 1

# loop through the bit recorders and calculate the result of single number
        res = 0
        for i in range(32):
            res <<= 1
            res += table[31 - i] % 3
            print(res, table[31 - i] % 3, 31 - i)
        return __convert(res)
if __name__ == "__main__":
    res = Solution().singleNumber([1, 1, 2, 3, 3, 3, 2, 2, 8, 1])
    res = Solution().singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
    print(res)


