class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -float('inf')
        curr = 0
        for i in nums:
            curr+=i
            if curr>=0:
                best = max(curr,best)
                print(i,best)
            else:
                best = max(curr,best)
                curr = 0
        return best
            
        