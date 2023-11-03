class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window_sum = sum(nums[0:k])
        avg = float( window_sum/k)
        for i in range(1,len(nums)-k+1):
            window_sum = window_sum-nums[i-1]+nums[i+k-1]
            avg = max(avg, float(window_sum/k))
            
        return avg
        
        