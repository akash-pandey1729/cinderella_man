class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        @lru_cache(None)
        def getPath(i,j):
            max_path_length = 1
            for x,y  in [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]:
                if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and (x,y) not in visited:
                    if matrix[x][y]>matrix[i][j]:
                        visited.add((x,y))
                        max_path_length = max(max_path_length, 1+ getPath(x,y))
                        visited.remove((x,y))
            return max_path_length

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited = set()
                ans = max(ans, getPath(i,j))
        return ans



