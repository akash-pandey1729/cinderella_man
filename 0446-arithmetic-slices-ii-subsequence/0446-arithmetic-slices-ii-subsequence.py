class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        cnt = [defaultdict(int) for _ in range(n)]
        
        subseq = 0
        for i,a in enumerate(nums):
            for j,b in enumerate(nums[:i]):
                cnt[i][a-b] += cnt[j][a-b] + 1
                subseq += cnt[j][a-b]
        
        return subseq