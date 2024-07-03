class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_idx, min_idx = 0,len(nums)-1
        min_ = min(nums)
        max_ = max(nums)
        for i in range(len(nums)):
            if nums[i]== min_:
                min_idx = i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]== max_:
                max_idx = i
                break
        total_swaps = min_idx + len(nums) - 1 - max_idx
        return total_swaps if min_idx <= max_idx else total_swaps - 1

        
        