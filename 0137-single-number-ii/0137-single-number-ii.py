class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l=1
        for i in range(0,len(nums)-1):
            # print(nums[i], l)
            if nums[i]==nums[i+1] and l!=3:
                l+=1
            elif nums[i]!=nums[i+1] and l==3:
                l = 1
            else:
                return nums[i]
        return nums[-1]



        
            

