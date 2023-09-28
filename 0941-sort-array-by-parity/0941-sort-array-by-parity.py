class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i]%2:
                ans.append(nums[i])
            else:
                ans.insert(0, nums[i])
        return ans
        