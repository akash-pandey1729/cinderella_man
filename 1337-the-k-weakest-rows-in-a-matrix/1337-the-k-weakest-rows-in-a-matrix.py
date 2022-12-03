class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            ones = 0
            for j in range(len(mat[0])):
                ones+= mat[i][j]
            heap.append([ones,i])
        heapq.heapify(heap)
        ans = []
        while k>0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans
            
                
        