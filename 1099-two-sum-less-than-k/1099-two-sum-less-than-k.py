class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        for j in range(len(nums)):
            t = bisect.bisect_left(nums,k-nums[j])-1
            if nums[j] + nums[t]<=k and t!=j and t>=0:
                ans = max(ans, nums[j] + nums[t])
        return ans
            
        