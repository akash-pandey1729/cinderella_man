class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = []
        self.curr_sum = 0
        

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.curr_sum+=val
        if len(self.nums) > self.size:
            temp = self.nums.pop(0)
            self.curr_sum -= temp
        return float(self.curr_sum/len(self.nums))






        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)