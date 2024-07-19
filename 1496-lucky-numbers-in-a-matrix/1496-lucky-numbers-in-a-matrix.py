class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        col_min = defaultdict(int)
        row_min = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                col_min[i] = matrix[i][j]
                row_min[j] = matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                col_min[i] = min(col_min[i], matrix[i][j])
        
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                row_min[j] = max(row_min[j], matrix[i][j])
        
        ans = []
        # print(row_min)
        # print(col_min)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if col_min[i]== matrix[i][j] and row_min[j]==matrix[i][j]:
                    ans.append(matrix[i][j])

        return ans

        

        


        