class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def bfs(stack, visited):
            d = 0
            while stack:
                n = len(stack)
                d+=1
                for _ in range(n):
                    i,j = stack.pop(0)
                    for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        if 0<=x<len(rooms) and 0<=y<len(rooms[0]) and (x,y) not in visited and rooms[x][y]!=-1:
                            rooms[x][y] = min(rooms[x][y], d)
                            visited.add((x,y))
                            stack.append((x,y))
        visited = set()
        stack = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    visited.add((i,j))
                    stack.append([i,j])
        bfs(stack, visited)





        