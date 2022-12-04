class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n =len(nums)
        prefixSum = [0]*n
        prefixSum[0] = nums[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1]+ nums[i]
        prefixAvg = [0]*n
        for i in range(n-1):
            prefixAvg[i] = abs(prefixSum[i]//(i+1) - (prefixSum[n-1]-prefixSum[i])//(n-i-1))
            
        prefixAvg[-1] = prefixSum[-1]//n
        _min = min(prefixAvg)
        for i in range(n):
            if prefixAvg[i]==_min:
                return i
            
            