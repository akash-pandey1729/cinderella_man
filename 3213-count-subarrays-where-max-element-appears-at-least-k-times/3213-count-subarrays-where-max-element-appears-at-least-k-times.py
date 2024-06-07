class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        _max = max(nums)
        if counter[_max]<k:
            return 0
        res,cnt, start = 0,0,0
        for i in range(len(nums)):
            if nums[i]==_max:
                cnt+=1
            while cnt==k:
                if nums[start]==_max:
                    cnt-=1
                start+=1
            res+=start
        return res



        
        


        