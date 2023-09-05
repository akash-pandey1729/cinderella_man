class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = ['(', '[', '{',]
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if stack and i==')' and stack[-1]=='(':
                    stack.pop()
                elif stack and i==']' and stack[-1]=='[':
                    stack.pop()
                elif stack and i=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        return len(stack)==0
        