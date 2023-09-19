class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = max(nums)
        for i in range(1, m+1):
            if c[i]>1:
                return i
        