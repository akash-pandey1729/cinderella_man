class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x,y = click
        if board[x][y]=="M":
            board[x][y]= "X"
            return board
        stack = [click]
        visited = set((x,y))
        while stack:
            n = len(stack)
            for _ in range(n):
                x,y = stack.pop(0)
                print(x,y)
                adj_mines = 0
                for i,j in [[x,y+1],[x,y-1],[x-1,y],[x+1,y],[x-1,y-1],[x+1,y+1], [x-1, y+1],[x+1,y-1]]:
                    if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=="M":
                        adj_mines+=1
                if adj_mines != 0:
                    board[x][y] = str(adj_mines)
                else:
                    board[x][y] = 'B'
                    for i,j in [[x,y+1],[x,y-1],[x-1,y],[x+1,y],[x-1,y-1],[x+1,y+1], [x-1, y+1],[x+1,y-1]]:
                        if 0<=i<len(board) and 0<=j<len(board[0]) and (i,j) not in visited:
                            visited.add((i,j))
                            stack.append([i,j])
        return board

                





        # while stack:
        #     n = len(stack)
        #     x,y = stack.pop(0)
        #     if board[x][y]=="M":
        #         board[x][y]= "X"
        #         return board
        #     adj_mines = 0
        #     for i,j in [[x,y+1],[x,y-1],[x-1,y],[x+1,y],[x-1,y-1],[x+1,y+1], [x-1, y+1],[x+1,y-1]]:
        #         if 0<=i<len(board) and 0<=j<len(board[0]):
        #             stack.append()








        
        