class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        earn = 0
        low, high = prices[0], prices[0]
        for p in prices:
            if p < high:
                print(earn)
                low = high = p
            else:
                high = p
                print(p, high, low)
                earn += high - low
                low = p
        return earn
if __name__ == '__main__':
    prices = [1, 2, 4]
    res = Solution().maxProfit(prices)
    print(res)
