class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0,0)
        dp = {}
        def steps(i):
            if i>len(cost):
                return float('inf')
            if i == len(cost):
                return 0
            if i not in dp:
                dp[i] = cost[i] + min(steps(i+1), steps(i+2))
            return  dp[i]
        return steps(0)