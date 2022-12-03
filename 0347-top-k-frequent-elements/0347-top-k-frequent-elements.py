class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in cnt.items()]
        heapify(maxHeap)
        
        ans = []
        for i in range(k):
            _, num = heappop(maxHeap)
            ans.append(num)
        return ans