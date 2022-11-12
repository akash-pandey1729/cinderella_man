class MedianFinder:

    def __init__(self):
        self.stream = []
        
    def addNum(self, num: int) -> None:
        bisect.insort_left(self.stream, num)
        

    def findMedian(self) -> float:
        t = len(self.stream)
        if t%2==1:
            return self.stream[t//2]
        else:
            return (self.stream[t//2 -1] + self.stream[t//2])/2