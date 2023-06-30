class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start, end = 0,0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i]>0:
                end = i+1
                start = i
                profit+= prices[end]-prices[start]
            else:
                start = i
                end = i
        return profit

            
        