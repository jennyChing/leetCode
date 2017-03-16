'''
135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings: return 0
        dp = [1] * len(ratings)
        # first scan from left to right and record if any r[i] > r[i - 1] incr
        for i in range(1, len(ratings)):
            dp[i] = dp[i - 1] + 1 if ratings[i] > ratings[i - 1] else 1

        # then scan from right to left and record if any r[i] > r[i + 1] decr
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
        return sum(dp)

if __name__ == '__main__':
    ratings = [1,0,2]
    ratings = [2,3,4,5,4,2,3]
    res = Solution().candy(ratings)
    print(res)

