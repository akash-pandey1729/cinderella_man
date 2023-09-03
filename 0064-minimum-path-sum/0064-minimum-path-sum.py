class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for i in grid[0]] for i in grid]
        def getSum(i,j):
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if i>=len(grid) or j>=len(grid[0]):
                return float('inf')
            if dp[i][j]==-1:
                dp[i][j] =  grid[i][j] + min(getSum(i+1,j), getSum(i,j+1))
            return dp[i][j]
        return getSum(0,0)




        