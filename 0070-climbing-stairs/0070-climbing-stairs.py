class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for i in range(n+1)]
        if n>1:
            dp[2] = 2
            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        