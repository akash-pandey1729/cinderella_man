class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        dict1 = {}
        ans = 0
        for num in nums:
            if num-1 in dict1:
                dict1[num] = dict1[num-1]+ 1
            else:
                dict1[num] = 1
            ans = max(ans, dict1[num])
        return ans
        