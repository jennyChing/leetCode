'''
421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''
class TrieNode(object):
    def __init__(self):
        self.memo = [None, None]
        self.val = 0

class Solution(object):
    def __init__(self):
        self.root = TrieNode()

    def reverse(self, n):
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # insert a number into the trie with mask (32-bit number)
        for n in nums:
            curr = self.root
            reverse_n = self.reverse(n)
            for i in range(32):
                bit = reverse_n & 1
                reverse_n >>= 1
                if curr.memo[bit] == None:
                    curr.memo[bit] = TrieNode()
                curr = curr.memo[bit]
            curr.val = n

        # search the largest complement (most left) for every num
        max_XOR = 0
        for n in nums:
            curr = self.root
            reverse_n = self.reverse(n)
            for i in range(32):
                bit = reverse_n & 1
                reverse_n >>= 1
                if curr.memo[bit ^ 1] != None: # is complement
                    curr = curr.memo[bit ^ 1]
                else:
                    curr = curr.memo[bit]
            max_XOR = max(max_XOR, n ^ curr.val)
        return max_XOR


if __name__ == "__main__":
    nums = [8, 2]
    res = Solution().findMaximumXOR(nums)
    print(res)
