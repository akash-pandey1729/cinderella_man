class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heapq.heapify(intervals)
        rooms = []
        heapq.heapify(rooms)
        ans = 0
        while intervals:
            while rooms and rooms[0]<= intervals[0][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, heapq.heappop(intervals)[1])
            ans = max(ans, len(rooms))
        return ans
        
        