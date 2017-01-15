'''
477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
'''
class Solution(object):
    def totalHammingDistance_n_square(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res += bin(nums[i] ^ nums[j]).count("1")
        return res

    def totalHammingDistance_n(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = [[0, 0] for _ in range(32)] # record 0s and 1s for each posit
        for n in nums:
            for pos in mask:
                pos[int(n % 2)] += 1
                n /= 2
        print(mask)
        return sum(x * y for x, y in mask)


if __name__ == "__main__":
    nums = [4, 14, 2, 2]
    res = Solution().totalHammingDistance_n(nums)
    print(res)
