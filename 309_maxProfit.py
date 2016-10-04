'''
309. Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
'''
class Solution(object):
    def __init__(self):
        self.isBuying = False
    def maxProfit(self, prices):
        '''
        for each p in prices, only 3 possible outcome: free, have or cool
        free: the max profit to be free to buy, do nothing for this one = max(free, cool)
        have: the max profit to holding the stock or buying now = max(have, free - p)
        cool: the max profit to sold the stock in current iteration = have + p
        '''
        free = 0
        have = cool = float('-inf')
        for p in prices:
            print(p, free - p, cool, have)
            free, have, cool = max(free, cool), max(have, free - p), have + p
            print(p, "free :", free, "have :", have, "cool: ", cool)
        return max(free, cool)
if __name__ == '__main__':
    res = Solution().maxProfit([1, 2, 3, 0, 2])
    print(res)


