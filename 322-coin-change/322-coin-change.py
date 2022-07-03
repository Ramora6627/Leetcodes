class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        # print(dp)

        for a in range(1,amount+1):
            # print("@",a)
            for c in coins:
                # print(c)
                if a - c >= 0:
                    # print(dp[a],dp[a-c])
                    dp[a] = min(dp[a],1 + dp[a-c])
        
        
        return dp[amount] if dp[amount] != amount +1 else -1

        