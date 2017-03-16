'''
60. Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        nums = [i for i in range(1, n + 1)]
        while len(nums) > 1:
            idx = (k - 1) // math.factorial(len(nums) - 1)
            print(idx, nums[idx], k)
            num = nums[idx]
            res += str(num)
            nums.remove(num)
            k -= idx * math.factorial(len(nums))
        res += str(nums[0])
        return res

if __name__ == "__main__":
    res = Solution().getPermutation(4, 13)
    print(res)
