class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dict1 = defaultdict(int)
        visited = set()
        def dfs(i,j, index):
            visited.add((i,j))
            grid[i][j] = index
            dict1[index]+=1
            for x,y in [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1 and (x,y) not in visited:
                    dfs(x,y,index)

        index = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== 1 and (i,j) not in visited:
                    dfs(i,j,index)
                    index+=1
        # print(dict1)
        # print(grid)
        def func(i,j):
            ans = 0
            seen = set()
            for x,y in [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] in dict1 and grid[x][y] not in seen:
                    seen.add(grid[x][y])
                    ans+= dict1[grid[x][y]]
            return ans+1

        ans_max = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    ans_max = max(ans_max, func(i,j))
        for key in dict1:
            ans_max = max(ans_max, dict1[key])
        return ans_max

        