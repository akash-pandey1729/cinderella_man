class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        min_range = [1 for i in nums]
        for i in range(len(nums)):
            temp = 1
            for j in range(i+1,len(nums)):
                if nums[j]>=nums[i]:
                    temp+=1
                else:
                    break
            min_range[i] = temp

        return sum(min_range)


        