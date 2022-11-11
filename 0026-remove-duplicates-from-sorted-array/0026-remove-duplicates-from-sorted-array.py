class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) != 1:
            l = 0
            r = 1
            while r<len(nums):
                if nums[l] == nums[r]:
                    nums[r] = "#"
                    r+=1
                else:
                    l = r
                    r = r+1
            l = 1
            r = 1
            while r<len(nums):
                if nums[r]=="#":
                    r+=1
                else:
                    nums[r], nums[l] = nums[l], nums[r]
                    l = l+1
                    r+=1
            while len(nums)>l:
                nums.pop()
                
                
            
            
        
            
            
        
        