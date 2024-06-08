class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict1 = {0:-1}
        cumSum = 0
        for i in range(len(nums)):
            cumSum+=nums[i]
            if cumSum%k in dict1:
                if i - dict1[cumSum%k]>=2:
                    return True
                continue
            elif cumSum%k not in dict1:
                dict1[cumSum%k] = i
        print(dict1)
        return False
                
            
        
#         Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).

        