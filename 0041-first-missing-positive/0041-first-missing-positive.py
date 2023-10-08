class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #find if there is a 1:
        if 1 not in nums:
            return 1
        n = len(nums)
        for idx in range(n):
            if nums[idx]<=0 or nums[idx]>n:
                nums[idx] = 1
        # print(nums)
        for idx in range(len(nums)):
            nums[abs(nums[idx])-1] = - abs(nums[abs(nums[idx])-1])
        # print(nums)
        for idx in range(len(nums)):
            if nums[idx]>0:
                return idx +1
        return n+1


        