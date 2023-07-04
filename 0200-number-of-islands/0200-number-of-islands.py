class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1" and (x,y) not in visited:
                    visited.add((x,y))
                    dfs(x,y)
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=="1":
                    visited.add((i,j))
                    dfs(i,j)
                    res+=1
        return res
        