class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp = {}
        def func(i,j):
            if i==m-1 and j==n-1:
                return 1
            if obstacleGrid[i][j]==1:
                return 0
            else:
                if (i,j) not in dp:
                    if i == m-1 and j!=n-1:
                        dp[(i,j)] =  func(i,j+1)
                    elif j==n-1 and i!=m-1:
                        dp[(i,j)] =  func(i+1,j)
                    else:
                        dp[(i,j)] =  func(i,j+1) + func(i+1,j)   
                return dp[(i,j)]  
        return func(0,0)
            


            
        