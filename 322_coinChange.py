'''
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # check boundary cases
        if amount == 0:
            return 0
        if coins == [1]:
            return amount
        def _get_change_making_matrix(set_of_coins, r):
             m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
        # why len(sets_of_coins) + 1:
             for i in range(r + 1):
                 m[0][i] = i
             return m

        count = 0
        m = _get_change_making_matrix(coins, amount)
        for r in range(1, amount + 1): # go through target n
            minC = float('inf')
            for c in range(1, len(coins) + 1): # go through number of set of coins
                # Just use the coin coins[c - 1].
                if coins[c - 1] == r:
                    m[c][r] = 1
                    count += 1
                # coins[c - 1] cannot be included.
                # We use the previous solution for making r,
                # excluding coins[c - 1].
                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]
                # We can use coins[c - 1].
                # We need to decide which one of the following solutions is the best:
                # 1. Using the previous solution for making r (without using coins[c - 1]).
                # 2. Using the previous solution for making r - coins[c - 1] (without using coins[c - 1]) plus this 1 extra coin.
                else:
                    minC = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
                    m[c][r] = -1 if minC
        print(m)
        return m[-1][-1] if m[-1][-1] != 1 else -1
if __name__ == "__main__":
    coins = [1, 2, 5]
    coints = [2]
    res = Solution().coinChange(coins, 3)
    print(res)
