class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        stack = [entrance]
        steps = 0
        visited = {(entrance[0],entrance[1])}
        while stack:
            # print(stack)
            n = len(stack)
            for i in range(n):
                x,y = stack.pop(0)
                if (x == len(maze)-1 or y == len(maze[0])-1 or x == 0 or y == 0) and maze[x][y] == "." and (x,y)!=(entrance[0],entrance[1]):
                    return steps
                for i,j in [[x-1,y],[x+1,y],[x,y-1],[x, y+1]]:
                    if 0<=i<len(maze) and 0<=j<len(maze[0]) and maze[i][j]=="." and (i,j) not in visited:
                        visited.add((i,j))
                        stack.append([i,j])
            steps+=1
        return -1
                
        