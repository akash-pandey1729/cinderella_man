class StockSpanner:
    def __init__(self):
        self.stack = []
# If the number is small, keep appending it to the stack, if greator, keep popping till you actually reach the number greator than current number..append the curr with count
    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
            
        
        self.stack.append([price, ans])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)