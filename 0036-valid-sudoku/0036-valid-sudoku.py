class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        def funcThreeCorssThree(p1,p2):
            a,b = p1
            x,y = p2
            M = set()
            for i in range(a,x):
                for j in range(b,y):
                    if board[i][j]== ".":
                        continue
                    elif board[i][j]!= "." and board[i][j] not in M:
                        M.add(board[i][j])
                    else:
                        # print("here", board[i][j] )
                        return False
            return True
        def help1():
            for i in range(0,n,3):
                for j in range(0,n,3):
                    if not funcThreeCorssThree([i,j], [i+3,j+3]):
                        return False
            return True
        def funcRow(r):
            M = set()
            for c in range(n):
                if board[r][c]==".":
                    continue
                elif board[r][c]!="." and board[r][c] not in M:
                    M.add(board[r][c])
                else:
                    return False
            return True
        def funcCol(c):
            M = set()
            for r in range(n):
                if board[r][c]==".":
                    continue
                elif board[r][c]!="." and board[r][c] not in M:
                    M.add(board[r][c])
                else:
                    return False
            return True
        def help2():
            for i in range(n):
                if not funcRow(i):
                    return False
            return True
        def help3():
            for i in range(n):
                if not funcCol(i):
                    return False
            return True
        return help1() and help2() and help3()
                
                    
                
            
        return help1()
                    
            
                    
                    
        