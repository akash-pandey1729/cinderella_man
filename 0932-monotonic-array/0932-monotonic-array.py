class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if sorted(nums) == nums or sorted(list(reversed(nums)))==list(reversed(nums)):
            return True
        return False
        