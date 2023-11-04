class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        nums.insert(0,0)
        dict1 = defaultdict(int)
        sum_so_far = 0
        ans = 0
        for i in range(len(nums)):
            sum_so_far+=nums[i]
            if sum_so_far not in dict1:
                dict1[sum_so_far] = i
            if sum_so_far-k in dict1:
                ans = max(ans, i - dict1[sum_so_far-k])
        return ans



        