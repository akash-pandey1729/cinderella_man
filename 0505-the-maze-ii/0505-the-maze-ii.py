class Solution:
    def shortestDistance(self, maze, start, destination):
        m,n,dict1 = len(maze),len(maze[0]),defaultdict(int)

        for i in range(m):
            for j in range(n):
                dict1[(i,j)] = float("inf")

        dict1[tuple(start)] = 0

        stack = [(start[0],start[1],0)]

        while stack:
            x,y,dist = heapq.heappop(stack)

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny,weight = x,y,0

                while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] != 1:
                    nx += dx
                    ny += dy
                    weight += 1

                if dict1[(nx,ny)] > dist + weight:
                    dict1[(nx,ny)] = dist + weight
                    heapq.heappush(stack,(nx,ny,dict1[(nx,ny)]))

        return dict1[tuple(destination)] if dict1[tuple(destination)] != float("inf") else -1


        

