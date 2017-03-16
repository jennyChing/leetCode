'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        forward = [0] * len(prices) # record the max-profit of [0,i] , end at most at pos i
        low = high = prices[0]
        for i, p in enumerate(prices):
            if p < low:
                low = p
            high = p
            forward[i] = high - low

        backward = [0] * len(prices) # record the max-profit of [i,len], start at most at pos i
        low = high = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > high:
                high = prices[i]
            low = prices[i]
            backward[i] = high - low
        res = 0
        curr_f, curr_b = forward[0], backward[0]
        for f, b in zip(forward, backward):
            curr_f = max(curr_f, f)
            res = max(res, curr_f + b)
        return res

if __name__ == '__main__':
    prices = [7, 9, 2, 3, 5, 2, 4]
    prices = [1,2,4]
    prices = [6,1,3,2,4,7]
    res = Solution().maxProfit(prices)
    print(res)

