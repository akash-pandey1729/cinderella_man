class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = Counter(nums)
        ans = []
        for i in dict1:
            ans.append((dict1[i],i))
        ans.sort()
        res = []
        t = 0
        n = len(ans)
        while(t<n):
            if(t==k):
                return res
            res.append(ans[n-1-t][1])
            t = t+1
        return res
        