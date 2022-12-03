class Solution:
    def furthestBuilding(self, A, bricks, ladders):
        heap = []
        for i in range(1,len(A)):
            d = A[i] - A[i-1]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i-1
        return len(A) - 1
                
            
                
            
            
            
        