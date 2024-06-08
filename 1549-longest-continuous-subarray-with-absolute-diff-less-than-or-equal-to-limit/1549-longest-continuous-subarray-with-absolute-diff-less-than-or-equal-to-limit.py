class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        res, j  = 0, 0
        i  = left = 0
        while i <len(nums):
            heapq.heappush(min_heap, (nums[i], i))
            heapq.heappush(max_heap, (-nums[i], i))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                j = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < j: heapq.heappop(max_heap)
                while min_heap[0][1] < j: heapq.heappop(min_heap)
            res = max(res, i - j + 1)
            i+=1
        return res
        


            



        