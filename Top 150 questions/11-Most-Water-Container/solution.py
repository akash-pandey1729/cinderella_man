class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        vol = 0
        while l<=r:
            vol = max(min(height[l], height[r])*(r-l), vol)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return vol
            

        