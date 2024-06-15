class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        print(nums)
        while k>1:
            heapq.heappop(nums)
            k-=1
        return -1*nums[0]

        