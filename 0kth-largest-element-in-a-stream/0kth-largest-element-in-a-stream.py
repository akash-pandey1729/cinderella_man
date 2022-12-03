class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst = nums
        self.k = k
        heapq.heapify(self.lst)
        
    def add(self, val: int) -> int:
        temp = []
        # self.lst.append(val)
        heapq.heappush(self.lst, val)
        while len(self.lst)>self.k:
            heapq.heappop(self.lst)
        return self.lst[0]
            
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)