class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes,l,ans = 0,0,0
        if k>=len(nums):
            return len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
            while zeroes>k and l<=i:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            ans = max(ans, i-l+1)
        return ans

        
        