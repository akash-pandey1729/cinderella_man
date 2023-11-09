class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        dp = defaultdict(int)
        self.dict1 = dp
        dp[(len(matrix)-1, len(matrix[0])-2)] = matrix[len(matrix)-1][len(matrix[0])-2]
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if i>=len(matrix) or j>=len(matrix[0]):
                    dp[(i,j)]==0
                else:
                    dp[(i,j)] = dp[(i+1,j)] + dp[(i,j+1)] + matrix[i][j] - dp[(i+1,j+1)]
                

    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.dict1)
        part1 = self.dict1[((row1,col1))]
        part2 = self.dict1[(row2+1,col1)]
        part3 = self.dict1[(row1,col2+1)]
        part4 = self.dict1[(row2+1,col2+1)]
        return part1 - part2 - part3 + part4
        


# Your Numself.matrix  object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)