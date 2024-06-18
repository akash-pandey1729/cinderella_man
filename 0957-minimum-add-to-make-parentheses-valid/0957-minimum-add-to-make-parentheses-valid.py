class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_ = 0
        bal = 0
        for i in range(len(s)):
            if s[i]=="(":
                open_+=1
            if s[i]==")" and open_:
                open_-=1
            elif s[i]==")" and not open_:
                bal+=1 
        return bal + open_
        