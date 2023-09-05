class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,value = 0,0
        ans = float('inf')
        for j in range(len(nums)):
            value+=nums[j]
            while value>=target:
                ans = min(ans, j-i+1)
                value-= nums[i]
                i+=1
        return ans if ans!= float('inf') else 0
