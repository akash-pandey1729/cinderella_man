class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        temp = nums[0]
        max_num = max(nums)
        nums = set(nums)
        while k>0:
            if temp not in nums:
                k-=1
            temp+=1
            if temp > max_num:
                return max_num + k
        # print(ans)
        return temp-1

        