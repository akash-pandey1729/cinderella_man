class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        l = 0
        max_middle = -1
        curr = 0
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>target and l<=i:
                curr-= nums[l]
                l+=1
            if curr == target:
                max_middle = max(max_middle, i-l+1)
        return len(nums) - max_middle if max_middle!=-1 else -1
        