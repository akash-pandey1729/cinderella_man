class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        dict1= set()
        for i in range(len(nums)):
            l,r = i-1, i+1
            while l>=0 and r<len(nums):
                if nums[l]+ nums[i] + nums[r]==0 and (nums[l], nums[i], nums[r]) not in dict1:
                    dict1.add((nums[l], nums[i], nums[r]))
                    ans.append([nums[l], nums[i], nums[r]])
                    l-=1
                    r+=1
                elif nums[l]+ nums[i] + nums[r] <0:
                    r+=1
                else:
                    l-=1
        return ans


        