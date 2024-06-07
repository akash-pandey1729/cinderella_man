class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        nums.append(nums[-1])
        ans = 0
        cnt, left = 0,0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                ans+= (i-left+1)*(i-left+2)//2
                left = i+1
        return ans

                

        