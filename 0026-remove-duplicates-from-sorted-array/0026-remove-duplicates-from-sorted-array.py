class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) != 1:
            l = 1
            r = 1
            while r<len(nums):
                if nums[r]==nums[r-1]:
                    r+=1
                else:
                    nums[l] = nums[r]
                    l = l+1
                    r+=1
            return l
            
                
                
            
            
        
            
            
        
        