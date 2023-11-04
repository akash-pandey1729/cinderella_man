class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        bal = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==0:
                bal-=1
            if nums[i]==1:
                bal+=1
            if bal==0:
                ans = max(ans, i+1)
            if bal in dict1:
                ans = max(ans, i - dict1[bal])
                # print("i is ", i, "ans is ", ans)
            else:
                dict1[bal] = i
        # print(dict1)
        return ans
        

        