class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def help(amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if amount not in dp:
                dp[amount] = float('inf')
                for coin in coins:
                    dp[amount]  = min(dp[amount] ,1 + help(amount-coin))
            return dp[amount] 
        return help(amount) if help(amount)!=float('inf') else -1
        
                
                
        
        
        