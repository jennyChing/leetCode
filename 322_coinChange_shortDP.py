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
import collections

class Solution(object):
    def BFScoinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [0] + [float('inf')] * amount
        q = collections.deque([0])
        while q:
            v = q.popleft()
            if v == amount:
                return table[-1]
            for c in coins:
                if v + c <= amount and table[v + c] == float('inf'):
                    table[v + c] = table[v] + 1
                    q.append(v + c)
        return -1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [0] + [float('inf')] * amount
        for c in coins:
            for r in range(c, amount + 1): # go through target n
                table[r] = min(table[r], table[r - c] + 1)
        print(table)
        return -1 if table[-1] == float('inf') else table[-1]

if __name__ == "__main__":
    coins = [1, 2, 5]
    coins = [2]
    res = Solution().coinChange(coins, 3)
    print(res)
