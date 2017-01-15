'''
474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
'''
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp array record first i elements in strs can form string length of idx or not with minimun use of m 0s and n 1s.
        dp_m = [0] + [float("inf") for _ in range(len(strs))]
        dp_n = [0] + [float("inf") for _ in range(len(strs))]
        # fill out dp array backward
        for i in range(1, len(strs) + 1): # use first i elements in strs
            for j in range(len(strs), 0, -1): # can form length of j strings
                ones = zeros = 0
                for c in strs[i - 1]:
                    if c == "0": ones += 1
                for c in strs[i - 1]:
                    if c == "1": zeros += 1

                if dp_m[j - 1] + ones <= m and dp_n[j - 1] + zeros <= n:
                    dp_m[j] = min(dp_m[j], dp_m[j - 1] + ones)
                    dp_n[j] = min(dp_n[j], dp_n[j - 1] + zeros)

        print(dp_m, dp_n)
        max_m, max_n = 0, 0
        for i, v in enumerate(dp_m):
            if v != float("inf"):
                max_m = i
                print(v, i)
        for i, v in enumerate(dp_n):
            if v != float("inf"):
                max_n = i
                print(i)
        return min(max_m, max_n)

    def findMaxForm_refer(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, len(strs)+1):
            zeroes, ones = strs[i-1].count('0'), strs[i-1].count('1')
# fill out from the back so that new input covered doesn't affect calculation
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= zeroes and k >= ones:
                        dp[j][k] = max(dp[j][k], 1 + dp[j-zeroes][k-ones])
            print("dp:", dp)
        return dp[m][n]

if __name__ == "__main__":
    strs = ["10", "0", "1"]
    m = 1
    n = 1
    strs = ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"]
    m = 30
    n = 30
    strs = ["1","0","1","0","1","0","1","0","1","0","1","0","1","0"]
    m = 3
    n = 3
    strs = ["10", "0001", "1110001", "1", "0"]
    m = 5
    n = 3
    res = Solution().findMaxForm_refer(strs, m, n)
    print(res)
