class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = [0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = -1

        for i in range(amount + 1):
            for j in range(len(coins)):
                if dp[i] >= 0:
                    if i + coins[j] > amount:
                        break
                    if dp[i + coins[j]] < 0:
                        dp[i + coins[j]] = dp[i] + 1
                    else:
                        dp[i + coins[j]] = min(dp[i + coins[j]], dp[i] + 1)
        if dp[amount] < 0:
            return -1
        return dp[amount]