class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def func(nums):
            if not nums:
                return [[]]
            else:
                res = []
                for i in range(len(nums)):
                    temp = nums.pop(i)
                    ans = func(nums)
                    for item in ans:
                        item.append(temp)
                        if item not in res:
                            res.append(item[:])
                    nums.insert(i, temp)
                return res
        return func(nums)
                        
                    
            
        
        