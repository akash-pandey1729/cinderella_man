class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        l = 1
        for i in range(len(nums)-1):
            if nums[i]< nums[i+1]:
                l+=1
            else:
                ans+= ((l)*(l+1)//2)
                l = 1
        ans+= ((l)*(l+1)//2)
        return ans
        