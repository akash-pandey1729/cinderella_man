class RateLimiter:

    def __init__(self, n: int, t: int):
        self.allowedList = []
        self.n = n
        self.t = t
        

    def shouldAllow(self, timestamp: int) -> bool:
        # print(self.allowedList)
        if len(self.allowedList)<self.n:
            # print("here, ", timestamp)
            self.allowedList.append(timestamp)
            return True
        
        idx = bisect.bisect_left(self.allowedList, timestamp - self.t +1)
        if len(self.allowedList) - idx < self.n:
            self.allowedList.append(timestamp)
            return True
        return False
            
        


# Your RateLimiter object will be instantiated and called as such:
# obj = RateLimiter(n, t)
# param_1 = obj.shouldAllow(timestamp)