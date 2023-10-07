class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = defaultdict(int)
        dict1[0] = 1
        ans = 0
        res = 0
        for i in range(len(nums)):
            ans+= nums[i]
            if ans-k in dict1:
                res+= dict1[ans-k]
            dict1[ans]+=1
        return res

            