class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_satisfied = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                already_satisfied+=customers[i]
                customers[i]=0
        window_sum = 0
        ans= 0
        l = 0
        for i in range(len(customers)):
            window_sum+=customers[i]
            if i-l<minutes:
                ans = max(ans, window_sum)
            else:
                window_sum-= customers[l]
                l+=1
                ans = max(ans, window_sum)
        return ans + already_satisfied





            

        