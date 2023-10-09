class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def left(l = 0,r= len(nums)-1):
            if l<=r:
                m = l+(r-l)//2
                if nums[m]>=target:
                    return left(l,m-1)
                if nums[m]<target:
                    return left(m+1, r)
            return l
        def right(l=0,r=len(nums)-1):
            if l<=r:
                m = l+(r-l)//2
                if nums[m]>target:
                    return right(l,m-1)
                if nums[m]<=target:
                    return right(m+1, r)
            return r
        ans = [-1,-1]
        if left()<len(nums) and nums[left()]==target:
            ans[0] = left()
        if right()<len(nums) and nums[right()] == target:
            ans[1] = right()
        return ans



        