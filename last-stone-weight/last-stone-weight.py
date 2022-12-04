class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heap.append(-stones[i])
        heapq.heapify(heap)
        while len(heap)>1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            heapq.heappush(heap,s1-s2)
        return -heap[0]
        