class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        temp = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                temp+=1
                ans = max(ans, temp)
            else:
                ans = max(ans, temp)
                temp = 1
        return ans
        