class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        adjacency = {}
        row = {}
        col= {}
        for i in range(len(stones)):
            if stones[i][0] in row:
                row[stones[i][0]].append(i)
            else:
                row[stones[i][0]] = [i]
            if stones[i][1] in col:
                col[stones[i][1]].append(i)
            else:
                col[stones[i][1]] = [i]
        # print(row)
        # print(col)
        visited = set()
        def dfs(idx):
            if idx not in visited:
                visited.add(idx)
                for i in row[stones[idx][0]] + col[stones[idx][1]]:
                    if i not in visited:
                        dfs(i)
        ans = 0
        for i in range(len(stones)):
            if i not in visited:
                ans+=1
                dfs(i)
        # print(visited)
        return len(visited)- ans
                
            
            
        