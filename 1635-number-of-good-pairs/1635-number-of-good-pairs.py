class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for key in cnt:
            ans+= ((cnt[key]*(cnt[key]-1))//2)
        return ans
        