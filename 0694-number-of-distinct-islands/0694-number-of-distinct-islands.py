class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        group = defaultdict(list)
        def dfs(i,j, id):
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1 and (x,y) not in visited:
                    group[id].append((x,y))
                    visited.add((x,y))
                    dfs(x,y,id)
        id = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    id+=1
                    group[id].append((i,j))
                    visited.add((i,j))
                    dfs(i,j,id)
                    # print(visited)
        # print(group)
        for id in group:
            x,y = group[id][0][0], group[id][0][1]
            group[id] = [[p[0]-x, p[1]-y] for p in group[id]]
        # print(group)
        def hashing(lst):
            hash = ""
            for l in lst:
                hash+= str(l[0])+"-"+str(l[1])+"-"
            return hash
        ans = set()
        for id in group:
            ans.add(hashing(group[id]))
        return len(ans)


        return len(group)


        

        