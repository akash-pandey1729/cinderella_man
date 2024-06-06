class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        curr = 0
        
        for i in range(len(nums)):
            target = nums[i]
            curr += target
            
            while (i - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            
            ans = max(ans, i - left + 1)

        return ans