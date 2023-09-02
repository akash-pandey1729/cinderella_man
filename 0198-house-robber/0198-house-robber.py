class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums)+2)]
        nums.insert(0,0)
        nums.insert(0,0)
        for i in range(2,len(dp)):
            dp[i] = max(nums[i]+ dp[i-2], dp[i-1])
        return dp[-1]

        