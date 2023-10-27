class MedianFinder:

    def __init__(self):
        self.heap_max = []
        self.heap_min = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap_max, -num)
        if len(self.heap_max)>len(self.heap_min):
            heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))

        if len(self.heap_min)>len(self.heap_max):
            heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
        
    def findMedian(self) -> float:
        if len(self.heap_min)==len(self.heap_max):
            return float((-self.heap_max[0] + self.heap_min[0])/2)
        return float(-self.heap_max[0])
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()