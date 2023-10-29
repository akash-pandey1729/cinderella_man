class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        bal = 0
        for i in range(len(s)):
            if not stack and s[i] == ')':
                bal+=1
            elif stack and s[i] ==')':
                stack.pop()
            else:
                stack.append('(')
        return bal + len(stack)


        