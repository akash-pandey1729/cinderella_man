class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        left,right = 1,len(word)-2
        leftDup = rightDup = 1
        while left<right:
            if word[left]==word[left-1]:
                leftDup += 1
            if word[right]==word[right+1]:
                rightDup += 1
                
            if rightDup<leftDup:
                word = word[::-1]
                break
                
            if word[left]!=word[left-1]:
                leftDup = 1
            if word[right]!=word[right+1]:
                rightDup = 1
            left += 1
            right -= 1
        def dfs(position, word, visited):
            # print(word)
            x, y = position[0], position[1]
            if len(word)==0:
                return True
            for i,j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]== word[0] and (i,j) not in visited:
                    visited.add((i,j))
                    t = dfs([i,j], word[1:], visited)
                    if t:
                        return t
                    visited.remove((i,j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    t = dfs([i,j], word[1:], {(i,j)})
                    if t:
                        return True
        return False
        