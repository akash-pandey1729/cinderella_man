class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        flag = True
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] >= nums[i]:
                continue
            else:
                flag = False
                l = i-1
                break
        # print(l, flag)
        if flag:
            nums.sort()
            return
        for i in range(len(nums)-1,l,-1):
            if nums[i]<=nums[l]:
                print("con")
                continue
            else:
                print("here",  nums[l], nums[i])
                nums[l], nums[i] = nums[i], nums[l]
                break
        i,j = l+1, len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        return
        
        