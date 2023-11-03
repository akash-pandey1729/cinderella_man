class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if not nums:
            return [[lower, upper]]
        if nums[len(nums)-1]<lower:
            return []
        if nums[0]>lower:
            res.append([lower, nums[0]-1])
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] + 1==nums[i+1]:
                continue
            else:
                start = nums[i]+1
                end = nums[i+1]-1
                res.append([start, end])
        if nums[len(nums)-1]< upper:
            res.append([nums[len(nums)-1]+1, upper])
        return res

        