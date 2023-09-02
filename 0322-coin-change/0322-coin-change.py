class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def func(amount = amount):
            if amount in coins:
                dp[amount] = 1
                return 1
            if amount<0:
                return float('inf')
            if amount==0:
                dp[amount] = 0
                return 0
            
            if amount not in dp:
                dp[amount] = float('inf')
                for coin in coins:
                    dp[amount] = min(dp[amount], 1+func(amount-coin))
            return dp[amount] 
        func()
        return dp[amount] if dp[amount]!=float('inf') else -1
        