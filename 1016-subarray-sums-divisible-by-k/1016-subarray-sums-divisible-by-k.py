class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        prefixSum = [i%k if i%k>=0 else i%k + k for i in prefixSum]
        # print(prefixSum)
        ans = 0
        dict1 = Counter(prefixSum)
        for key in dict1:
            ans+= dict1[key]* (dict1[key]-1)//2
        return ans
