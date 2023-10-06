class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if len(customers)<=minutes:
            return sum(customers)
        sum_array = []
        for num in customers:
            if sum_array:
                sum_array.append(sum_array[-1]+ num)
            else:
                sum_array.append(num)
        satisfied = [0]* len(customers)
        satisfied[0] = customers[0] if not grumpy[0] else 0
        for i in range(1, len(customers)):
            if not grumpy[i]:
                satisfied[i] = satisfied[i-1] + customers[i]
            else:
                satisfied[i] = satisfied[i-1]
        ans = 0
        satisfied.insert(0,0)
        sum_array.insert(0,0)
        for i in range(len(customers)-minutes+1):
            ans = max(ans, sum_array[i+minutes]-sum_array[i] + satisfied[i] + satisfied[-1]-satisfied[i+minutes])
        return ans
       








        