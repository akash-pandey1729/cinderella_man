class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        import numpy as np 
        #storing the indexes of the elements in dictionary a with values as a key
        counter={}
        for i in range(len(nums)):
            if nums[i] not in counter:
                counter[nums[i]]=[i]
            else:
                counter[nums[i]].append(i)
        dp={}
        def rec(i,d,c):
            if (i,d,c) in dp:
                return dp[(i,d,c)]
            
            total=0
            if c>=3:
                total+=1
            if nums[i]+d in counter:
                for j in counter[nums[i]+d]:
                    if j>i:
                        total+=rec(j,d,c+1)
            dp[(i,d,c)]=total
            return total
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):             
                ans+=rec(j,nums[j]-nums[i],2)
        return ans