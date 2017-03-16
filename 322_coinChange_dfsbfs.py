class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # faster: find shortest path with BSF search and count the number of coins used
        if not amount: return 0
        dp = [0] + [sys.maxint for _ in range(amount)]
        bfs_q = collections.deque([0]) # start with amount = 1 往上加 until sum up to amount
        while bfs_q:
            v = bfs_q.popleft()
            if v == amount:
                return dp[-1]
            for c in coins:
                if v + c <= amount and dp[v + c] == sys.maxint:
                    bfs_q.append(v + c)
                    dp[v + c] = dp[v] + 1
        return -1

        # try dfs (sort the coins first)
        if not amount: return 0

        coins.sort(reverse=True)
        def dfs(start, remain, cnt): # similar to combination sum using dfs
            if not remain:
                self.cnt = min(self.cnt, cnt)
            for i in range(start, len(coins)): # use for loop from start index to all coins to skip coins to get all possibility
                if coins[i] <= remain < coins[i] * (self.cnt - cnt): # upperbound makes sure this dfs's cnt could < self.cnt
                    dfs(i, remain - coins[i], cnt + 1) # can reuse i!
        self.cnt = sys.maxint
        for i in range(len(coins)):
            dfs(i, amount, 0)
        return self.cnt if self.cnt != sys.maxint else -1

        # slow: use dp table to record coins change combinations, lookup idx (amount - coints value)
        dp = [0] + [sys.maxint for _ in range(amount)]
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if coins[i] == j: # compare with j not dp[j]!
                    dp[j] = 1
                if coins[i] <= j:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] != sys.maxint else -1
