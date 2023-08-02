class MinStack:

    def __init__(self):
        self.list = []
        self.track_min = []
        self.i = 0
        
    def push(self, val: int) -> None:
        self.i+=1
        self.list.append(val)
        if not self.track_min or self.track_min[-1][1]>=val:
            self.track_min.append((self.i,val))
        else:
            self.track_min.append(self.track_min[-1])
        

    def pop(self) -> None:
        temp = float('inf')
        if self.list:
            temp = self.list.pop()
        if temp == self.track_min[-1][1]:
            t = self.track_min[-1]
            while self.track_min and self.track_min[-1]== t:
                self.track_min.pop()   

    def top(self) -> int:
        return self.list[-1]
        
    def getMin(self) -> int:
        return self.track_min[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()