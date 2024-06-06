class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = [[-reward1[i]+ reward2[i], reward1[i], reward2[i]] for i in range(len(reward1))]
        heapq.heapify(heap)
        # print(heap)
        ans = 0
        while heap:
            _, r1, r2 = heapq.heappop(heap)
            if k>0:
                ans+=r1
                k-=1
            else:
                ans+= r2
        return ans






        