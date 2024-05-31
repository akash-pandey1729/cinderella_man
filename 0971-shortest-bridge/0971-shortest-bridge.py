class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island_one = set()
        def dfs(i,j):
            for x,y in [[i+1,j], [i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1 and (x,y) not in island_one:
                    island_one.add((x,y))
                    dfs(x,y)
        seen_one = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not seen_one:
                    seen_one = True
                    island_one.add((i,j))
                    dfs(i,j)
                    break
            if seen_one:
                break
        for p in island_one:
            grid[p[0]][p[1]]=2

        def bfs():
            stack = [(0,p[0],p[1]) for p in island_one]
            visited = copy.deepcopy(island_one)
            while stack:
                n = len(stack)
                for _ in range(n):
                    d,i,j = stack.pop(0)
                    if grid[i][j]==1:
                        return d
                    for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and (x,y) not in visited:
                            if grid[x][y] == 1 or grid[x][y]==0:
                                visited.add((x,y))
                                stack.append((d+1,x,y))
        return bfs()-1


        


        