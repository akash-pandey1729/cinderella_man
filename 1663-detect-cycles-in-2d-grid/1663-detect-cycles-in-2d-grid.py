class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        main = set()
        def dfs(i,j,p,q):
            for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if (x,y) in visited and (x,y)!=(p,q):
                    return True
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and (x,y) not in visited and grid[x][y]==grid[i][j] and (x,y)!=(p,q):
                    visited.add((x,y))
                    main.add((x,y))
                    if dfs(x,y,i,j):
                        return True
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in main:
                    visited = set()
                    visited.add((i,j))
                    main.add((i,j))
                    if dfs(i,j,i,j):
                        return True
        return False


        