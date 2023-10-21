class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-1*float('inf'))
        nums.insert(0,-1*float('inf'))
        def getpeak(l,r):
            if l<=r:
                m = l + (r-l)//2
                if nums[m]>nums[m+1] and nums[m]>nums[m-1]:
                    return m
                elif nums[m]>=nums[m-1]:
                    return getpeak(m+1,r)
                else: 
                    return getpeak(l,m-1)
            return -1
        return getpeak(0,len(nums)-1)-1