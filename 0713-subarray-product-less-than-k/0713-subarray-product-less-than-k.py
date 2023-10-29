class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, prod, ans = 0,1,0
        for i in range(len(nums)):
            prod*=nums[i]
            while prod>=k and l<=i:
                prod/= nums[l]
                l+=1
            if prod<k:   
                ans+= i-l+1
        return ans
            

        