class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left(l = 0,r= len(nums)-1):
            if l<=r:
                m = l+(r-l)//2
                if m-1>=0 and nums[m]==target and nums[m-1]!=target:
                    return m
                if m==0 and nums[0]==target:
                    return m
                if nums[m]>=target:
                    return left(l,m-1)
                if nums[m]<target:
                    return left(m+1, r)
            return -1
        
        def right(l=0,r=len(nums)-1):
            if l<=r:
                m = l+(r-l)//2
                if m+1<len(nums) and nums[m]==target and nums[m+1]!=target:
                    # print("here1", m)
                    return m
                if m+1==len(nums) and nums[m]==target:
                    return m
                if nums[m]>target:
                    return right(l,m-1)
                if nums[m]<=target:
                    return right(m+1, r)
            return -1
        # print(right())
        return [left(), right()]



        