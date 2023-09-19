class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp  = {}
        def dfs( n: int, subset_sum: int) -> bool:
            
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            if (n,subset_sum) not in dp:
                dp[(n,subset_sum)]  = False
                dp[(n,subset_sum)] = (dfs(n - 1, subset_sum - nums[n - 1])
                    or dfs( n - 1, subset_sum))
            return dp[(n,subset_sum)] 

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs( n - 1, subset_sum)