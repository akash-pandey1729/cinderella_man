class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        arr = [[startTime[i], endTime[i], profit[i]] for i in range(len(profit))]
        arr.sort(key = lambda x:x[0])
        
        dp = {}
        def func(i=0):
            if i>=len(arr):
                return 0
            if i not in dp:
                j = bisect.bisect_left(arr, arr[i][1], key = lambda x:x[0])
                dp[i]= max(func(i+1), arr[i][2]+ func(j))
            return dp[i]
        return func()
            
            
            
            
        