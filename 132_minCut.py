'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

if __name__ == '__main__':
    s = "aab"
    res = Solution().minCut(s)
    print(res)

