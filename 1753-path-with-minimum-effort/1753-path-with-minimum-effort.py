import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap,(0,0,0))
        distance = [[float('inf') for i in range(len(heights[0]))] for j in range(len(heights))]
        distance[0][0] = 0
        visited = set()
        while heap:
            d, i, j= heapq.heappop(heap)
            visited.add((i,j))
            for x,y in [[i,j+1],[i,j-1],[i+1,j],[i-1,j]]:
                if 0<=x<len(heights) and 0<=y<len(heights[0]) and (x,y) not in visited:
                    cost = abs(heights[i][j]-heights[x][y])
                    if distance[x][y] > max(cost, distance[i][j]):
                        distance[x][y] = max(cost, distance[i][j])
                        heapq.heappush(heap, (distance[x][y], x, y))
        return distance[-1][-1]




        