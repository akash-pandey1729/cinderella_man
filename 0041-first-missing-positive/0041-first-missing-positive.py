class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cnt = set(nums)
        max_ = max(cnt)
        if max_<1:
            return 1
        for i in range(1,max_+2):
            if i not in cnt:
                return i

        