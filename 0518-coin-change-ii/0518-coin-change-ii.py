class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp ={}
        def func(amount, index):
            if amount == 0:
                return 1
            if amount<0 or index==len(coins):
                return 0
            if (amount, index) not in dp:
                dp[(amount, index)] = func(amount - coins[index], index) + func(amount, index+1)
            return dp[(amount, index)] 
        return func(amount,0)
        
        